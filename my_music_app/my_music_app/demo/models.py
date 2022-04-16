from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

EXCEPTION_MESSAGE = "Ensure this value contains only letters, numbers, and underscore."


def validator_only_letters_number_underscores(value):
    for char in value:
        if not char.isdigit() and not char.isalpha() and not char == '_':
            raise ValidationError(EXCEPTION_MESSAGE)


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_VALUE = 2
    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_VALUE),
            validator_only_letters_number_underscores,
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_AND_B_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'OTHER'

    GENRE_TYPES = (POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=(
            (g, g) for g in GENRE_TYPES),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
