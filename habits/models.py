from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Habit(models.Model):
    """Модель привычки с характеристиками."""

    title = models.CharField("Привычка", max_length=255)

    description = models.TextField("Описание", blank=True, null=True)

    time_required = models.PositiveIntegerField("Время выполнения, мин.", default=1)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",  # <-- Теперь связь в обе стороны идеальна!
        verbose_name="Автор",
    )

    is_healthy = models.BooleanField("Здоровая привычка", default=True)

    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
      )

    class Meta:
        verbose_name ="привычка"
        verbose_name_plural ="Привычки"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title[:20]