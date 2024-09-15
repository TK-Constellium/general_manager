# Generated by Django 5.1.1 on 2024-09-15 20:07

import django.core.validators
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=50)),
                (
                    "number",
                    models.CharField(
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator("^AP\\d{5}$")
                        ],
                    ),
                ),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "total_capex_value",
                    models.DecimalField(
                        db_index=True, decimal_places=10, max_digits=30, null=True
                    ),
                ),
                ("total_capex_unit", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalProject",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "number",
                    models.CharField(
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator("^AP\\d{5}$")
                        ],
                    ),
                ),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "total_capex_value",
                    models.DecimalField(
                        db_index=True, decimal_places=10, max_digits=30, null=True
                    ),
                ),
                ("total_capex_unit", models.CharField(max_length=30, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical project",
                "verbose_name_plural": "historical projects",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
