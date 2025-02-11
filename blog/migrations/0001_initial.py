# Generated by Django 5.1.3 on 2024-12-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="заголовок")),
                ("body", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "views_count",
                    models.IntegerField(default=0, verbose_name="Просмотров"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
    ]
