# Generated by Django 3.2 on 2022-12-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20221217_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token2',
            field=models.CharField(blank=True, max_length=256, verbose_name='Токен'),
        ),
    ]
