# Generated by Django 3.2.7 on 2021-09-30 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_dummy'),
        ('orders', '0002_auto_20210930_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Select Game'),
        ),
    ]
