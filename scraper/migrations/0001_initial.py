# Generated by Django 3.2.5 on 2021-07-19 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
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
                    "path",
                    models.CharField(
                        max_length=1000, verbose_name="Page Path"
                    ),
                ),
                (
                    "has_js",
                    models.BooleanField(
                        default=False, verbose_name="JS Rendered"
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Website",
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
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="Name of Site",
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=4, verbose_name="Unique Code"),
                ),
                ("url", models.URLField(unique=True, verbose_name="Base URL")),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["id"], name="scraper_web_id_b2efaa_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["-id"], name="scraper_web_id_85a07e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["name"], name="scraper_web_name_1a38b3_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["-name"], name="scraper_web_name_ae38d2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["code"], name="scraper_web_code_6050aa_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="website",
            index=models.Index(
                fields=["-code"], name="scraper_web_code_40d36e_idx"
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="scraper.website",
            ),
        ),
        migrations.AddIndex(
            model_name="page",
            index=models.Index(
                fields=["id"], name="scraper_pag_id_f5790b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="page",
            index=models.Index(
                fields=["-id"], name="scraper_pag_id_536707_idx"
            ),
        ),
    ]
