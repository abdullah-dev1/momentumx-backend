import random
import string
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)

def generate_new_password(length: int = 10) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

async def send_reset_email(email: str, new_password: str, name: str):
    html = f"""
    <div style="font-family: Arial, sans-serif; max-width: 500px; margin: auto; padding: 30px; border-radius: 10px; background: #f9f9f9;">
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #6C63FF;">⚡ MomentumX</h1>
        </div>
        <h2 style="color: #333;">Password Reset</h2>
        <p style="color: #555;">Hi <strong>{name}</strong>,</p>
        <p style="color: #555;">We received a request to reset your password. Here is your new temporary password:</p>
        <div style="background: #6C63FF; color: white; font-size: 22px; font-weight: bold; text-align: center; padding: 16px; border-radius: 8px; letter-spacing: 2px; margin: 20px 0;">
            {new_password}
        </div>
        <p style="color: #555;">Please login with this password and change it from your profile immediately.</p>
        <p style="color: #999; font-size: 12px; margin-top: 30px;">If you did not request this, please ignore this email. Your account is safe.</p>
        <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
        <p style="color: #999; font-size: 12px; text-align: center;">MomentumX — Build. Track. Dominate.</p>
    </div>
    """

    message = MessageSchema(
        subject="🔐 Your MomentumX Password Reset",
        recipients=[email],
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)