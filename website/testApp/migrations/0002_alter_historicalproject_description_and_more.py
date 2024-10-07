# Generated by Django 5.1.1 on 2024-10-03 19:48

import django.core.validators
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testApp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalproject",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="number",
            field=models.CharField(
                max_length=7,
                validators=[django.core.validators.RegexValidator("^AP\\d{4,5}$")],
            ),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="total_capex_unit",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalproject",
            name="total_capex_value",
            field=models.DecimalField(
                blank=True, db_index=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="number",
            field=models.CharField(
                max_length=7,
                validators=[django.core.validators.RegexValidator("^AP\\d{4,5}$")],
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="total_capex_unit",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="total_capex_value",
            field=models.DecimalField(
                blank=True, db_index=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
        migrations.CreateModel(
            name="Derivative",
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
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "estimated_weight_value",
                    models.DecimalField(
                        blank=True,
                        db_index=True,
                        decimal_places=10,
                        max_digits=30,
                        null=True,
                    ),
                ),
                (
                    "estimated_weight_unit",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("estimated_volume", models.IntegerField(blank=True, null=True)),
                (
                    "changed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testApp.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalDerivative",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "estimated_weight_value",
                    models.DecimalField(
                        blank=True,
                        db_index=True,
                        decimal_places=10,
                        max_digits=30,
                        null=True,
                    ),
                ),
                (
                    "estimated_weight_unit",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("estimated_volume", models.IntegerField(blank=True, null=True)),
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
                    "changed_by",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
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
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="testApp.project",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical derivative",
                "verbose_name_plural": "historical derivatives",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]