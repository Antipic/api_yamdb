from django.core.mail import send_mail
from api_yamdb.settings import EMAIL_FROM

def send_confirmation_code(email, username, confirmation_code):
    """Oтправляем на почту подтверждения."""
    send_mail(
        subject='Код подтверждения',
        message=(
            f'Отправте ваш код подтверждения: {confirmation_code}\n'
            'на эндпоинт /api/v1/auth/token/ в следующем формате\n'
            '{\n'
            f'    "username": "{username}",\n'
            f'    "confirmation_code": "{confirmation_code}"\n'
            '}\n'
        ),
        from_email=EMAIL_FROM,
        recipient_list=(email,),
        fail_silently=False,
    )
