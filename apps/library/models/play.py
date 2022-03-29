from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint

from apps.core.models import BaseModel
from apps.core.utils import slugify
from apps.info.models import Festival
from apps.library.validators import year_validator


class ProgramType(BaseModel):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Название программы",
    )
    slug = models.SlugField(
        max_length=40,
        verbose_name="Slug",
        unique=True,
    )

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Play(BaseModel):
    name = models.CharField(
        max_length=70,
        verbose_name="Название пьесы",
    )
    city = models.CharField(
        max_length=200,
        verbose_name="Город",
        blank=True,
        null=True,
    )
    year = models.PositiveSmallIntegerField(
        validators=[year_validator],
        verbose_name="Год написания пьесы",
        blank=True,
        null=True,
    )
    url_download = models.FileField(
        max_length=200,
        upload_to="plays",
        verbose_name="Текст пьесы",
        blank=True,
        help_text="Для пьес Любимовки должен быть загружен файл",
    )
    url_reading = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Ссылка на читку",
        unique=True,
    )
    program = models.ForeignKey(
        ProgramType,
        on_delete=models.PROTECT,
        related_name="plays",
        verbose_name="Программа",
    )
    festival = models.ForeignKey(
        Festival,
        on_delete=models.PROTECT,
        related_name="plays",
        verbose_name="Фестиваль",
        blank=True,
        null=True,
        help_text="Для пьес Любимовки должен быть выбран Фестиваль",
    )
    published = models.BooleanField(
        verbose_name="Опубликовано",
        default=True,
    )
    link = models.URLField(
        max_length=500,
        verbose_name="Ссылка",
        blank=True,
    )

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=("name", "festival"),
                name="unique_play",
            ),
        )
        verbose_name = "Пьеса"
        verbose_name_plural = "Пьесы"

    def __str__(self):
        return self.name + ("" if self.published else " <— не опубликована —>")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        if self.program.slug != "other_plays":
            if not self.url_download.name:
                raise ValidationError("Для пьесы Любимовки неоходимо загрузить файл")
            if self.festival is None:
                raise ValidationError("У пьесы Любимовки должен быть фестиваль")
            self.link = ""
        if self.program.slug == "other_plays":
            if self.link == "":
                raise ValidationError("Необходимо указать ссылку на другую пьесу")
            self.published = False
        return super().clean()
