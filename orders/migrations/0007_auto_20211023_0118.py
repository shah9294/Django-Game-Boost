# Generated by Django 3.2.7 on 2021-10-22 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_delete_review'),
        ('accounts', '0024_delete_review'),
        ('orders', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.buyer'),
        ),
        migrations.AddField(
            model_name='review',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='games.game'),
        ),
        migrations.AddField(
            model_name='review',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.seller'),
        ),
    ]
