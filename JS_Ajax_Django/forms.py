from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

from .models import BaseContact

class LandingForm(forms.ModelForm):
    class Meta:
        model = BaseContact
        fields = ('name', 'email', 'phone')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':u"Ваше ім'я*"}),
            'email': forms.TextInput(attrs={'placeholder':u'Ваш E-mail*'}),
            'phone': forms.TextInput(attrs={'placeholder':u'Контактний телефон*'}),
        }

    def send_email(self):
        form_data = self.cleaned_data
        subject = 'Заполнение формы'
        from_email = 'From email <%s>'%settings.EMAIL_HOST_USER
        recipient_list = ['info@example.com',]
        message = 'Здравствуйте,\nНовая заполненая форма \nИмя: %s\nТелефон: %s\nE-mail: %s\nС уважением, ...'%(
            form_data['name'],
            form_data['email'],
            form_data['phone'],
        )
        msg = EmailMessage(
            subject,
            message,
            from_email,
            recipient_list,
        )
        msg.send()