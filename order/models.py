from django.db import models


class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE)

    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(max_length=150, verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.boat} от {self.email}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
