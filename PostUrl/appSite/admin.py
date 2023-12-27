from django.contrib import admin
from .models import FormUser

@admin.register(FormUser)
class FormUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'age'] # отображение полей в админке
    list_display_links = ['name', 'email'] # для кликабельности в админке
    list_filter = ['age'] # для фильтрации в админке
