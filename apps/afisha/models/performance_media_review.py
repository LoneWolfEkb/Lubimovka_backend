from django.db import models

from apps.afisha.models import Performance
from apps.content_pages.utilities import path_by_app_label_and_class_name
from apps.core.models import BaseModel, Image
from apps.core.utils import delete_image_with_model


class PerformanceImage(Image):
    performance = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE,
        related_name="images_in_block",
        verbose_name="Изображения спектакля",
    )


class PerformanceMediaReview(BaseModel):
    media_name = models.CharField(
        max_length=100,
        verbose_name="Название медиа ресурса",
    )
    text = models.TextField(
        max_length=2000,
        verbose_name="Текст отзыва",
    )
    image = models.ImageField(
        upload_to=path_by_app_label_and_class_name,
        verbose_name="Логотип медиа ресурса",
    )
    performance = models.ForeignKey(
        Performance,
        on_delete=models.PROTECT,
        related_name="media_reviews",
        verbose_name="Спектакль",
    )
    url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Ссылка на отзыв",
        unique=True,
    )
    pub_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Медиа отзыв на спектакль"
        verbose_name_plural = "Медиа отзывы на спектакль"

    def __str__(self):
        return self.media_name

    def save(self, *args, **kwargs):
        this = PerformanceMediaReview.objects.filter(id=self.id).first()
        if this:
            if this.image != self.image:
                this.image.delete(save=False)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        delete_image_with_model(self, PerformanceMediaReview, *args, **kwargs)


class PerformanceReview(BaseModel):
    reviewer_name = models.CharField(
        max_length=100,
        verbose_name="Имя зрителя",
    )
    text = models.TextField(
        max_length=2000,
        verbose_name="Текст отзыва",
    )
    performance = models.ForeignKey(
        Performance,
        on_delete=models.PROTECT,
        related_name="reviews",
        verbose_name="Спектакль",
    )
    url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Ссылка на отзыв",
        unique=True,
    )
    pub_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Отзыв зрителя на спектакль"
        verbose_name_plural = "Отзывы зрителей на спектакль"

    def __str__(self):
        return self.reviewer_name
