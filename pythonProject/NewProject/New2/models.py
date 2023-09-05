from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Human(models.Model):
    Name = models.CharField(max_length=30, verbose_name='Имя')
    Surname = models.CharField(max_length=30, verbose_name='Фамилия')
    Patronymic = models.CharField(max_length=30, verbose_name='Пароль')
    Date_of_birth = models.DateTimeField(verbose_name='Дата рождения')
    Gender = models.CharField(max_length=1, verbose_name='Пол')
    Photo = models.ImageField(upload_to='media', verbose_name='Фото')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессии')

    def get_absolute_url(self):
        return reverse_lazy('View_humans', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-Date_of_birth']


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессии')

    def get_absolute_url(self):
        return reverse_lazy('Profession', kwargs={'profession_id': self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']

