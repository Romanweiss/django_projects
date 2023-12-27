from django.db import models


class FormUser(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        null = False,
        max_length = 40,
        default = 'Неизвестно'
    )

    email = models.EmailField(
        verbose_name = 'Электронная почта',
        null = False,
        unique = True, # проверка поля на  уникальность 
        db_index = True # для ускорения фильтрации, если есть поле uniq
    )

    age = models.IntegerField(
        verbose_name = 'Возраст',
        null = False
    )

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Контактную информация'
        verbose_name_plural = 'Контактная информация'