from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, EmailValidator


class Feedback(models.Model):  # Модель обратной связи
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'Не проверено'
        CHECKED = 1, 'Проверено'

    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(blank=False, null=False, verbose_name='email')
    message = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Сообщение')
    check_status = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]),
                                                         Status.choices)), default=Status.UNCHECKED,
                                       verbose_name='Статус проверки')

    def __str__(self):
        return f'{self.name} - {self.email} - {self.message}'


class Calculator(models.Model):  # Модель кредитного калькулятора
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(100000), MaxValueValidator(5000000)])
    term = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])  # срок
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2,
                                        validators=[MinValueValidator(0), MaxValueValidator(100)])  # процентная ставка
    monthly_payment = models.CharField(max_length=255)
    total_payment = models.CharField(max_length=255)
    total_interest = models.CharField(max_length=255)


class Loan(models.Model):  # Модель результата расчета
    amount = models.CharField(max_length=255)
    term = models.CharField(max_length=255)  # срок
    interest_rate = models.CharField(max_length=255)  # процентная ставка
    monthly_payment = models.CharField(max_length=255)
    total_payment = models.CharField(max_length=255)
    total_interest = models.CharField(max_length=255)

    def __str__(self):
        return f'сумма:{self.amount}, срок:{self.term}, ставка:{self.interest_rate} %'


class LoanApplication(models.Model):  # Модель кредитной заявки
    customer = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='Расчеты калькулятора')
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    date_birth = models.DateField(verbose_name='Дата рождения')  # прописать валидацию даты рождения
    passport_series = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        verbose_name='Серия паспорта')  # прописать валидацию серии паспорта
    passport_number = models.IntegerField(
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
        verbose_name='Номер паспорта')  # прописать валидацию номера паспорта
    registration_address = models.CharField(max_length=255, validators=[
        RegexValidator(r'^[А-ЯЁа-яё\s,.-]+$')], verbose_name='Адрес регистрации')  # прописать логику адреса регистрации
    email = models.EmailField(validators=[EmailValidator()],
                              verbose_name='Адрес электронной почты')  # прописать валидацию эл.почты

    def __str__(self):
        return (f'{self.name} - {self.last_name}-{self.patronymic}- {self.date_birth}- {self.passport_series}-'
                f' {self.passport_number}- {self.registration_address}- {self.email}')


