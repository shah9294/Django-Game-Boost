# Generated by Django 3.2.7 on 2021-10-12 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20211012_1201'),
        ('games', '0013_sellergame'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='clicks',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of clicks recieved'),
        ),
        migrations.AlterField(
            model_name='sellergame',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_games', to='accounts.seller'),
        ),
        migrations.AlterField(
            model_name='sellergame',
            name='seller_description_of_game',
            field=models.TextField(blank=True, null=True, verbose_name='Seller description of Game'),
        ),
    ]
