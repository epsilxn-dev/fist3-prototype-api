from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(for_who: list[str], title: str, message: str):
    send_mail(
        subject=title,
        message=message,
        from_email=None,
        recipient_list=for_who,
        fail_silently=True
    )


def send_email_template(for_who: list[str], title: str, template: str, context: dict = None):
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    send_mail(
        subject=title,
        message=plain_message,
        from_email=None,
        recipient_list=for_who,
        html_message=html_message
    )
