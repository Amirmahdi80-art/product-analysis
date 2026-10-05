import os
import logging

from openai import OpenAI, APIError, APITimeoutError, RateLimitError
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

AI_API_KEY = os.environ.get("AI_API_KEY")
if not AI_API_KEY:
    raise RuntimeError("AI_API_KEY is not set. Add it to your .env file.")

client = OpenAI(api_key=AI_API_KEY, base_url="https://api.deepseek.com")


def ai_give_answers(messages, temperature=0.4, max_tokens=4000, retries=3):
    import time

    last_exc = None
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            logger.info(
                "DeepSeek call ok: prompt=%s completion=%s total=%s",
                getattr(response.usage, "prompt_tokens", "?"),
                getattr(response.usage, "completion_tokens", "?"),
                getattr(response.usage, "total_tokens", "?"),
            )
            return response.choices[0].message.content
        except (RateLimitError, APITimeoutError) as e:
            last_exc = e
            time.sleep(2**attempt)
        except APIError as e:
            status = getattr(e, "status_code", None)
            if status and 400 <= status < 500:
                raise  # don't retry client errors
            last_exc = e
            time.sleep(2**attempt)
    raise last_exc


def ai_persian_system_prompt():
    return (
        "تو یک تحلیل‌گر موجودی هستی. یک آرایه JSON از ردیف‌های محصول به تو داده می‌شود. "
        "هر ردیف قبلاً توسط یک موتور قانون دسته‌بندی شده است؛ ستون‌های status_tag، action و "
        "next_recommended_action خروجی این موتور هستند. "
        "وظیفه تو یافتن الگوهای بین‌ردیفی، علامت‌گذاری موارد مبهم و خلاصه کردن وضعیت دسته است. "
        "ستون‌های عددی را بازمحاسبه نکن و قانون جدید نساز. "
        "پاسخ را کاملاً به زبان فارسی بده."
    )
