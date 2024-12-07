from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    description = models.TextField(
        'Текст задачи',
    )
    create_date = models.DateTimeField(
        verbose_name='Дата и время создания задачи',
        auto_now_add=True,
    )
    author_task = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_task',
        verbose_name='Автор задачи',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return str(self.description)[:40]


class AppointedPerformer(models.Model):
    performer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Ответственный',
        null=True,
        blank=True,
    )
    performer_appointed_date = models.DateTimeField(
        verbose_name='Дата и время назначения исполнителя',
        auto_now_add=True,
    )
    task = models.OneToOneField(
        Task, on_delete=models.CASCADE, primary_key=True,
    )

    def __str__(self) -> str:
        return str(self.performer)


class CompletedTask(models.Model):
    task_completed_date = models.DateTimeField(
        verbose_name='Дата и время выполнения',
        auto_now_add=True,
    )
    task_completed = models.OneToOneField(
        Task, on_delete=models.CASCADE, primary_key=True,
    )
    performer_task_completed = models.OneToOneField(
        AppointedPerformer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.task_completed_date)


class VerifiedTask(models.Model):
    task_verified = models.OneToOneField(
        Task, on_delete=models.CASCADE, primary_key=True,
    )
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Ревъюер',
        null=True,
        blank=True,
    )
    task_verified_date = models.DateTimeField(
        verbose_name='Дата и время проверки',
        auto_now_add=True,
    )
    verified_task_completed = models.OneToOneField(
        CompletedTask,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.reviewer)
