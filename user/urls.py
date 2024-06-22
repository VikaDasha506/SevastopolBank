from django.urls import path
from . import views

app_name = 'user'  # Пространство имен для приложения

urlpatterns = [
    path('feedback/', (views.FeedBack.as_view()), name='feedback'),
    path('feedback/thanks/', (views.ThanksForFeedback.as_view()), name='thanks'),
    path('customer/', (views.CustomerCreate.as_view()), name='calculator'),
    path('customer/result', (views.CustomerResult.as_view()), name='result'),
    path('save_loan_data/', views.save_loan_data, name='loan_data'),
    path('customer/loan_applications/', (views.CustomerLoanApplications.as_view()), name='customer_loan_application'),
    path('customer/loan_application_success/', (views.LoanApplicationSuccess.as_view()), name='loan_application_success'),
]
#<int:customer_id>/