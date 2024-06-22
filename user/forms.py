from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Feedback, Calculator, LoanApplication, Loan


class FeedbackForm(ModelForm):
    name = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = ['amount', 'term', 'interest_rate', 'monthly_payment', 'total_payment', 'total_interest']


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'term', 'interest_rate', 'monthly_payment', 'total_payment', 'total_interest']


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['name', 'last_name', 'patronymic', 'date_birth', 'passport_series', 'passport_number',
                  'registration_address', 'email']
