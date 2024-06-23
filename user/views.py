from django.shortcuts import render
from .models import Feedback, Calculator, LoanApplication, Loan
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class FeedBack(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    redirect_field_name = 'next'
    success_url = reverse_lazy('user:thanks')
    fields = ['name', 'email', 'message']

    def form_valid(self, form):
        return super().form_valid(form)


class ThanksForFeedback(TemplateView):
    template_name = 'feedback_thanks.html'


@csrf_protect
# @csrf_exempt
def save_loan_data(request):
    if request.method == 'POST':
        # Получаем данные из запроса
        amount = request.POST.get('amount')
        term = request.POST.get('term')
        interest_rate = request.POST.get('interestRate')
        monthly_payment = request.POST.get('monthlyPayment')
        total_payment = request.POST.get('totalPayment')
        total_interest = request.POST.get('totalInterest')

        # Создаем новый объект Loan и сохраняем данные
        loan = Loan(
            amount=amount,
            term=term,
            interest_rate=interest_rate,
            monthly_payment=monthly_payment,
            total_payment=total_payment,
            total_interest=total_interest
        )
        loan.save()

        # Сохраняем ID расчета кредита в сессии
        request.session['loan_id'] = loan.id

        return render(request, 'result.html', {'loanData': loan})
    else:
        return render(request, 'error_page.html', {'message': 'Invalid request'})


class CustomerCreate(CreateView):
    model = Calculator
    template_name = 'calculator.html'
    fields = ['amount', 'term', 'interest_rate', 'monthly_payment', 'total_payment', 'total_interest']


class CustomerResult(TemplateView):
    template_name = 'result.html'


class CustomerLoanApplications(CreateView):
    model = LoanApplication
    template_name = 'loan_application.html'
    fields = ['name', 'last_name', 'patronymic', 'date_birth', 'passport_series', 'passport_number',
              'registration_address', 'email']
    redirect_field_name = 'next'
    success_url = reverse_lazy('user:loan_application_success')

    def form_valid(self, form):
        # Получаем ID расчета кредита из сессии
        loan_id = self.request.session.get('loan_id')
        if loan_id:
            loan = Loan.objects.get(id=loan_id)
            form.instance.customer = loan
            return super().form_valid(form)
        else:
            form.add_error(None, 'Loan calculation not found')
            return self.form_invalid(form)


class LoanApplicationSuccess(TemplateView):
    template_name = 'loan_application_success.html'
