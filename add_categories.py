# add_colors.py
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Import your Color model (adjust the import path to match your app)
from salesoptimizer.models import ProductCategories  # Replace with your actual app and model name

# Color data
categories = [
    {"category_code": "17", "category_name": "ادکلن"},
    {"category_code": "18", "category_name": "پالتو"},
    {"category_code": "50", "category_name": "پلیور بافت یقه 5 سانت"},
    {"category_code": "42", "category_name": "پلیور بافت یقه گرد ساده"},
    {"category_code": "58", "category_name": "پلیور بافت یقه گرد طرح دار"},
    {"category_code": "72", "category_name": "پلیور بافت یقه هفت"},
    {"category_code": "57", "category_name": "پلیور دورس"},
    {"category_code": "89", "category_name": "پلیور سلانیک یقه هفت"},
    {"category_code": "56", "category_name": "پلیور سلانیک یقه گرد"},
    {"category_code": "41", "category_name": "پلیور نیم زیپ"},
    {"category_code": "79", "category_name": "پلیور یقه اسکی"},
    {"category_code": "88", "category_name": "پلیور یقه پیراهنی"},
    {"category_code": "86", "category_name": "پولوشرت آستین بلند"},
    {"category_code": "93", "category_name": "پولوشرت ساده"},
    {"category_code": "94", "category_name": "پولوشرت طرح دار"},
    {"category_code": "21", "category_name": "پیراهن آستین بلند ساده"},
    {"category_code": "97", "category_name": "پیراهن آستین بلند چهار خانه"},
    {"category_code": "66", "category_name": "پیراهن آستین بلند راه راه"},
    {"category_code": "20", "category_name": "پیراهن آستین بلند طرح دار"},
    {"category_code": "22", "category_name": "پیراهن آستین کوتاه ساده"},
    {"category_code": "23", "category_name": "پیراهن آستین کوتاه طرح دار"},
    {"category_code": "75", "category_name": "پیراهن جین آستین کوتاه"},
    {"category_code": "74", "category_name": "پیراهن جین آستین بلند"},
    {"category_code": "52", "category_name": "پیراهن ضخیم"},
    {"category_code": "68", "category_name": "پیراهن نیمه ضخیم"},
    {"category_code": "95", "category_name": "تی شرت ساده"},
    {"category_code": "28", "category_name": "تی شرت آستین بلند"},
    {"category_code": "96", "category_name": "تی شرت طرح دار"},
    {"category_code": "27", "category_name": "تی شرت یقه اسکی"},
    {"category_code": "60", "category_name": "جعبه کفش"},
    {"category_code": "14", "category_name": "جلیقه"},
    {"category_code": "53", "category_name": "جلیقه شمعی"},
    {"category_code": "33", "category_name": "جوراب ساق دار"},
    {"category_code": "36", "category_name": "جوراب ضخیم"},
    {"category_code": "91", "category_name": "جوراب مچی"},
    {"category_code": "34", "category_name": "جوراب نیم ساق"},
    {"category_code": "19", "category_name": "زیر پوش رکابی"},
    {"category_code": "84", "category_name": "زیرپوش آستین دار"},
    {"category_code": "92", "category_name": "ست"},
    {"category_code": "13", "category_name": "سویشرت"},
    {"category_code": "76", "category_name": "سویشرت بافت"},
    {"category_code": "49", "category_name": "سویشرت شمعی"},
    {"category_code": "62", "category_name": "شلوار پارچه ای رگولار"},
    {"category_code": "26", "category_name": "شلوار اسلش"},
    {"category_code": "69", "category_name": "شلوار اسلش کتان"},
    {"category_code": "30", "category_name": "شلوار اسلش ورزشی"},
    {"category_code": "48", "category_name": "شلوار پارچه ای"},
    {"category_code": "32", "category_name": "شلوار پارچه ای اسکینی"},
    {"category_code": "61", "category_name": "شلوار پارچه ای اسلیم"},
    {"category_code": "24", "category_name": "شلوار جین"},
    {"category_code": "12", "category_name": "شلوار جین رگولار"},
    {"category_code": "10", "category_name": "شلوار جین اسکینی"},
    {"category_code": "63", "category_name": "شلوار جین اسلش"},
    {"category_code": "11", "category_name": "شلوار جین اسلیم"},
    {"category_code": "25", "category_name": "شلوار کتان"},
    {"category_code": "15", "category_name": "شلوار کتان اسلیم"},
    {"category_code": "31", "category_name": "شلوارک"},
    {"category_code": "81", "category_name": "شورت اسلیپ"},
    {"category_code": "83", "category_name": "شورت پادار"},
    {"category_code": "82", "category_name": "شورت نیم پا"},
    {"category_code": "16", "category_name": "کاپشن"},
    {"category_code": "78", "category_name": "کاپشن جین"},
    {"category_code": "51", "category_name": "کاپشن ضخیم"},
    {"category_code": "87", "category_name": "کاپشن کتان"},
    {"category_code": "90", "category_name": "کارت هدیه"},
    {"category_code": "47", "category_name": "کت تک رسمی"},
    {"category_code": "46", "category_name": "کت تک روزمره"},
    {"category_code": "80", "category_name": "کت جین"},
    {"category_code": "77", "category_name": "کت کتان"},
    {"category_code": "67", "category_name": "کراوات"},
    {"category_code": "44", "category_name": "کفش روزمره"},
    {"category_code": "73", "category_name": "کفش بوت"},
    {"category_code": "43", "category_name": "کفش رسمی"},
    {"category_code": "59", "category_name": "کفش نیم بوت رسمی"},
    {"category_code": "70", "category_name": "کفش نیم بوت روزمره"},
    {"category_code": "45", "category_name": "کفش ورزشی"},
    {"category_code": "65", "category_name": "کفی کفش"},
    {"category_code": "39", "category_name": "کلاه"},
    {"category_code": "40", "category_name": "کلاه ضخیم"},
    {"category_code": "38", "category_name": "کمربند رسمی"},
    {"category_code": "37", "category_name": "کمربند روزمره"},
    {"category_code": "99", "category_name": "کیف"},
    {"category_code": "71", "category_name": "هودی"},
]


def add_categories():
    """Add colors to the database"""
    for category in categories:
        ProductCategories.objects.create(category_code=category["category_code"], category_name=category["category_name"])
        print(f"{category['category_code']} was saved successfully.")


if __name__ == "__main__":
    add_categories()
