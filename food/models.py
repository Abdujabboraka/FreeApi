from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategorialar'


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='narxi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='kategoriyasi')
    description = models.TextField(blank=True, null=True, verbose_name='matn')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'


class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='xaridor')
    items = models.ManyToManyField(Food,related_name='taomlar')
    status = models.CharField(max_length=10, verbose_name='status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan_sanasi')

    def __str__(self):
        return f'Xaridor {self.customer.username} - {self.status}'

    class Meta:
        verbose_name = 'Xarid'
        verbose_name_plural = 'Xaridlar'
