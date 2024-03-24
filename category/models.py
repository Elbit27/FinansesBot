from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
