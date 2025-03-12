import uuid
import yookassa
from yookassa import Payment

from config import settings

yookassa.Configuration.configure(settings.YOOKASSA_SHOP_ID, settings.YOOKASSA_SECRET_KEY)

async def create_payments(amount: float, currency: str='RUB', description: str='пожертвования'):
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": currency
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/ваш_бот"
        },
        "capture": True,
        "description": description
    }, idempotence_key)
    return payment