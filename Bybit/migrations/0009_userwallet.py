# Generated by Django 5.1.1 on 2024-12-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bybit', '0008_user_firstname_user_lastname_user_nickname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField(unique=True)),
                ('wallet_address', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
