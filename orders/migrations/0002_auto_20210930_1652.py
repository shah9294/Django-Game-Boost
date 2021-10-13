# Generated by Django 3.2.7 on 2021-09-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=999, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('at', 'Active'), ('cp', 'Completed'), ('dl', 'Delivered'), ('cd', 'Canceled')], max_length=2, verbose_name='Status'),
        ),
    ]
