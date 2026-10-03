# add_colors.py
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Import your Color model (adjust the import path to match your app)
from salesoptimizer.models import Color  # Replace with your actual app and model name

# Color data
colors = [
    {"code": "01", "color": "سفید"},
    {"code": "02", "color": "مشکی"},
    {"code": "03", "color": "زرد"},
    {"code": "04", "color": "سبز"},
    {"code": "05", "color": "آبی"},
    {"code": "06", "color": "قرمز"},
    {"code": "07", "color": "بنفش"},
    {"code": "08", "color": "قهوه ای"},
    {"code": "09", "color": "خاکستری"},
    {"code": "10", "color": "صورتی"},
    {"code": "11", "color": "نارنجی"},
    {"code": "12", "color": "یاسی"},
    {"code": "13", "color": "سرمه ای"},
    {"code": "14", "color": "کرم"},
    {"code": "15", "color": "زرشکی"},
    {"code": "16", "color": "نقره ای"},
    {"code": "18", "color": "برنزی"},
    {"code": "19", "color": "دودی"},
    {"code": "20", "color": "عسلی"},
    {"code": "21", "color": "گلبه ای"},
    {"code": "22", "color": "ذغالی"},
    {"code": "23", "color": "آبی نفتی"},
    {"code": "24", "color": "سرمه ای تیره"},
    {"code": "25", "color": "سبز یشمی"},
    {"code": "26", "color": "آبی روشن"},
    {"code": "27", "color": "سبز تیره"},
    {"code": "28", "color": "خردلی"},
    {"code": "29", "color": "قهوه ای تیره"},
    {"code": "30", "color": "سبز روشن"},
    {"code": "32", "color": "خاکستری روشن"},
    {"code": "33", "color": "سرمه ای روشن"},
    {"code": "34", "color": "لیمویی"},
    {"code": "35", "color": "بنفش روشن"},
    {"code": "36", "color": "خاکستری تیره"},
    {"code": "37", "color": "عسلی تیره"},
    {"code": "38", "color": "کرم روشن"},
    {"code": "39", "color": "آبی تیره"},
    {"code": "40", "color": "قهوه ای روشن"},
    {"code": "41", "color": "طوسی"},
    {"code": "42", "color": "آجری"},
    {"code": "43", "color": "شیری"},
    {"code": "44", "color": "سبز مغز پسته ای"},
    {"code": "45", "color": "فیلی"},
    {"code": "47", "color": "سبز کله غازی"},
    {"code": "48", "color": "صورتی روشن"},
    {"code": "49", "color": "زرشکی تیره"},
    {"code": "50", "color": "بنفش تیره"},
    {"code": "51", "color": "سبز سدری"},
    {"code": "52", "color": "آبی آسمانی"},
    {"code": "53", "color": "کرم تیره"},
    {"code": "54", "color": "استخوانی"},
    {"code": "56", "color": "زرد روشن"},
    {"code": "57", "color": "زرد تیره"},
    {"code": "58", "color": "آبی فیروزه ای"},
    {"code": "59", "color": "لیمویی تیره"},
    {"code": "60", "color": "سبز فسفری"},
    {"code": "61", "color": "صورتی تیره"},
    {"code": "62", "color": "زرشکی روشن"},
    {"code": "64", "color": "عسلی روشن"},
    {"code": "65", "color": "سبز زیتونی"},
    {"code": "66", "color": "آبی کاربنی"},
    {"code": "67", "color": "گلبه ای روشن"},
    {"code": "68", "color": "لیمویی روشن"},
    {"code": "69", "color": "گلبه ای تیره"},
    {"code": "70", "color": "سبز ارتشی"},
    {"code": "71", "color": "طوسی تیره"},
]


def add_colors():
    """Add colors to the database"""
    for color in colors:
        Color.objects.create(code=color["code"], color=color["color"])
        print(f"{color['code']} was saved successfully.")


if __name__ == "__main__":
    add_colors()
