# Generated by Django 5.0.4 on 2024-10-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]