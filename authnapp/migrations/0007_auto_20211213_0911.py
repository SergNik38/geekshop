# Generated by Django 2.2.24 on 2021-12-13 09:11

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0006_auto_20211212_0448"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 15, 9, 11, 44, 816629, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
