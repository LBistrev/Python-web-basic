from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name'
    )

    image_url = models.URLField(
        verbose_name='URL'
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    TITLE_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
    )
