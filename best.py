import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.db import transaction
from django.db.models import Sum
from salesoptimizer.models import TwelveMonthAnalysisStore


def main():
    # 1. Reset all flags first (so re-runs are idempotent)
    TwelveMonthAnalysisStore.objects.update(best_store=False)

    # 2. Aggregate the sum for every (product_code, sales_office_id)
    rows = (
        TwelveMonthAnalysisStore.objects
        .values('product_code', 'sales_office_id')
        .annotate(total=Sum('total_sold_12_months'))
    )

    # 3. Group by product_code so we can find the max per product
    by_product = {}
    for r in rows:
        by_product.setdefault(r['product_code'], []).append(r)

    updates = []  # list of (product_code, sales_office_id) to flip to True

    for product_code, entries in by_product.items():
        # skip products with no sales-office rows
        if not entries:
            continue

        # find the highest sum
        max_total = max(e['total'] for e in entries)

        # if the highest sum is zero (or None), nobody wins
        if max_total is None or max_total == 0:
            continue

        # all stores that tie for the max get flagged
        for e in entries:
            if e['total'] == max_total:
                updates.append((product_code, e['sales_office_id']))

    # 4. Apply updates in bulk
    print(f'Flagging {len(updates)} (product, store) pairs as best_store=True')

    with transaction.atomic():
        for product_code, sales_office_id in updates:
            TwelveMonthAnalysisStore.objects.filter(
                product_code=product_code,
                sales_office_id=sales_office_id,
            ).update(best_store=True)

    print('Done.')


if __name__ == '__main__':
    main()