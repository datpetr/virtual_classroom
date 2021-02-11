from django.db import models


role_choices = [
    ('one', 'студент'),
    ('two', 'преподоватль')
]


class Registration(models.Model):
    first_name = models.CharField('имя', max_length=30, help_text='Введите имя')
    last_name = models.CharField('фамилия', max_length=30, help_text='Введите фамилию')
    registration_email = models.EmailField('e-mail', max_length=30, help_text='Введите e-mail')
    registration_role = models.CharField('роль', max_length=10, choices=role_choices, help_text='Выберите роль')
    registration_password = models.CharField('пароль', max_length=40, help_text='Введите пароль')
