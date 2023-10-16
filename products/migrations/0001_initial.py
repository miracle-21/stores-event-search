# Generated by Django 4.2.6 on 2023-10-16 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=200)),
            ],
            options={"db_table": "stores",},
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("plus", models.CharField(max_length=100)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=13, null=True),
                ),
                ("img", models.CharField(max_length=1000)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.store"
                    ),
                ),
            ],
            options={"db_table": "products",},
        ),
    ]
