# Generated by Django 3.2.7 on 2021-09-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_cnic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit_card_number',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='cnic',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
