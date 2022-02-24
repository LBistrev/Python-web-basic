from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from expenses_tracker.web.vaidators import validate_only_letters, ImageMaxSizeInMbValidator


class Profile(models.Model):

    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        verbose_name='Link to Image',
        null=True,
        blank=True,
        validators=(
            ImageMaxSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):

    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField(
        verbose_name='Link to Image:'
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()

    class Meta:
        ordering = ('title', 'price',)
