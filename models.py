from peewee import *

itr_db = SqliteDatabase('itr.db')

class Person(Model):
    last_name = FixedCharField(
        max_length=20,
        null=False,
        verbose_name='Фамилия'
    )
    name = FixedCharField(
        max_length=20,
        null=False,
        verbose_name='Имя'
    )
    patronymic = FixedCharField(
        max_length=20,
        null=False,
        verbose_name='Отчество'
    )
    is_admitting = BooleanField(
        verbose_name='Допускающий'
    )
    is_issuing = BooleanField(
        verbose_name='Допускающий'
    )
    is_approving = BooleanField(
        verbose_name='Допускающий'
    )

    class Meta:
        database = itr_db
        order_by = ('last_name',)
        