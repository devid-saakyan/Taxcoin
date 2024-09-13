# Generated by Django 5.1.1 on 2024-09-13 11:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TelegramId', models.BigIntegerField(unique=True)),
                ('BybitId', models.CharField(max_length=50, unique=True)),
                ('Balance', models.FloatField()),
                ('RegistrationDate', models.DateTimeField()),
                ('RegisteredWithReferral', models.BooleanField(default=False)),
            ],
        ),
    ]
