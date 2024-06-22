from django.contrib import admin
from .models import Feedback, LoanApplication


# http://127.0.0.1:8000/admin/
# логин Anna
# пароль admin

# admin.site.register(Card)
@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # поля,отображаемые в админке
    list_display_links = ('name', 'message')  # кликабельные поля
    list_per_page = 25  # количество элементов на странице
    actions = ['make_checked', 'make_unchecked']
    change_form_template = 'admin/feedback_form.html'

    @admin.action(description='Отметить обращение как проверенное')
    def make_checked(self, request, queryset):
        queryset.update(check_status=True)

    @admin.action(description='Отметить обращение как непроверенное')
    def make_unchecked(self, request, queryset):
        queryset.update(check_status=False)


@admin.register(LoanApplication)
class LoanApplication(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'patronymic', 'date_birth', 'passport_series', 'passport_number',
                    'registration_address', 'email', 'customer')  # поля,отображаемые в админке
    list_per_page = 25  # количество элементов на странице
    actions = ['make_checked', 'make_unchecked']
    change_form_template = 'admin/change_form.html'

    @admin.action(description='Отметить заявку как проверенную')
    def make_checked(self, request, queryset):
        queryset.update(check_status=True)

    @admin.action(description='Отметить заявку как непроверенную')
    def make_unchecked(self, request, queryset):
        queryset.update(check_status=False)
