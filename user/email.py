from django.core.mail import send_mail
from templated_mail.mail import BaseEmailMessage

from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from django.template.loader import render_to_string

from djoser.conf import settings
from django.conf import settings as base_settings


class CustomEmailMessage(BaseEmailMessage):
    def send(self, *args, **kwargs):
        context = self.get_context_data()
        subject = '[NECICADA] Активация аккаунта'

        html_data = render_to_string(self.template_name, context)

        send_mail(subject, None, 'NECACADA <necicada.test@gmail.com>', [
                  context['user_email']], html_message=html_data)


class UserActivationEmail(CustomEmailMessage):
    template_name = 'email/activation.html'

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get('user')
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        context["base_url"] = 'http://127.0.0.1:8080'
        context["user_name"] = user.username
        context["user_email"] = user.email
        return context
