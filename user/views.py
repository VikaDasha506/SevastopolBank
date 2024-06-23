from django.shortcuts import render
from .models import Feedback, Calculator, LoanApplication, Loan
from .forms import FeedbackForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class FeedBack(CreateView):
    model = Feedback  # Указываем модель, с которой работает представление
    form = FeedbackForm  # Указываем класс формы обратной связи
    template_name = 'feedback.html'  # Указываем шаблон, который будет использоваться для отображения формы
    redirect_field_name = 'next'  # имя параметра запроса, в котором хранится URL-адрес, на который пользователь должен быть перенаправлен после успешного входа в систему.
    success_url = reverse_lazy('user:thanks')  # URL для перенаправления после успешной отправки формы
    fields = ['name', 'email', 'message']

    #
    def form_valid(self, form):
        # Метод, вызываемый при успешной валидации формы.
        return super().form_valid(form)

    # def get_success_url(self):
    #     if self.request.POST.get('next', '').strip():
    #         return self.request.POST.get('next')
    #     return reverse_lazy('user:thanks')


class ThanksForFeedback(TemplateView):
    """Представление для отображения страницы с сообщением об успешной отправке формы:"""
    template_name = 'feedback_thanks.html'


@csrf_exempt  # Отключаем CSRF для этого запроса для примера
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
    """Представление для отображения страницы с сообщением об успешной отправке формы:"""
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
            form.instance.customer = loan  # Связываем заявку с расчетом кредита
            return super().form_valid(form)
        else:
            form.add_error(None, 'Loan calculation not found')
            return self.form_invalid(form)


class LoanApplicationSuccess(TemplateView):
    """Представление для отображения страницы с сообщением об успешной отправке формы:"""
    template_name = 'loan_application_success.html'