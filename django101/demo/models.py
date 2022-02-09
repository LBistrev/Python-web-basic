from django.db import models

# Create your models here.
# тук дефинираме модела, който после ще стане реално таблица

# този клас представлява таблица в базата ни от данни

# Code first approach


class Task(models.Model):
    # в моделите не правим инит
    # това са клас атрибути
    title = models.CharField(
        max_length=15,
        null=False,
    )
    text = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f'{self.id}: {self.title}'
