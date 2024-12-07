# Generated by Django 5.1.3 on 2024-11-24 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('description', models.TextField(verbose_name='Текст задачи')),
                (
                    'create_date',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата и время создания задачи',
                    ),
                ),
                (
                    'author_task',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='author_task',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Автор задачи',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='AppointedPerformer',
            fields=[
                (
                    'performer_appointed_date',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата и время назначения исполнителя',
                    ),
                ),
                (
                    'task',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to='task_treker.task',
                    ),
                ),
                (
                    'performer',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Исполнитель',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                (
                    'task_completed_date',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Дата и время выполнения',
                    ),
                ),
                (
                    'task_completed',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to='task_treker.task',
                    ),
                ),
                (
                    'performer_task_completed',
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='task_treker.appointedperformer',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='VerifiedTask',
            fields=[
                (
                    'task_verified',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to='task_treker.task',
                    ),
                ),
                (
                    'task_verified_date',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата и время проверки'
                    ),
                ),
                (
                    'reviewer',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Ревъюер',
                    ),
                ),
                (
                    'verified_task_completed',
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='task_treker.completedtask',
                    ),
                ),
            ],
        ),
    ]
