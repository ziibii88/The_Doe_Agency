# Generated by Django 3.2.5 on 2021-07-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraper", "0003_auto_20210725_1741"),
    ]

    operations = [
        migrations.CreateModel(
            name="Check",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="Active Status"
                    ),
                ),
                (
                    "error",
                    models.TextField(
                        blank=True, null=True, verbose_name="Error message"
                    ),
                ),
                (
                    "is_success",
                    models.BooleanField(
                        default=False, verbose_name="Success status"
                    ),
                ),
                (
                    "completed_at",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Datetime of Completion",
                    ),
                ),
                (
                    "proxies",
                    models.ManyToManyField(
                        related_name="proxies", to="scraper.Proxy"
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at", "-completed_at"),
            },
        ),
        migrations.AddIndex(
            model_name="check",
            index=models.Index(
                fields=["id"], name="scraper_che_id_c935d1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="check",
            index=models.Index(
                fields=["-id"], name="scraper_che_id_57c581_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="check",
            index=models.Index(
                fields=["-created_at"], name="scraper_che_created_713a01_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="check",
            index=models.Index(
                fields=["-completed_at"], name="scraper_che_complet_8ad61f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="check",
            index=models.Index(
                fields=["-created_at", "-completed_at"],
                name="scraper_che_created_2681aa_idx",
            ),
        ),
    ]