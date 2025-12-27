from tabnanny import verbose
from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(max_length  = 30, verbose_name = "Название сайта")
    description = models.TextField(verbose_name = "Описание сайта")
    logo = models.ImageField(verbose_name = "лого")
    phone_number = models.CharField(max_length = 30, verbose_name = "Номкр телефона")
    email = models.EmailField(verbose_name = "емаил")
    address = models.CharField(max_length = 30, verbose_name = "Адрес")

    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информация о сайте"
