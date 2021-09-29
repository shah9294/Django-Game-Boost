# Generated by Django 3.2.7 on 2021-09-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_user_cnic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='about_info',
            field=models.TextField(blank=True, max_length=500, verbose_name='About info'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cnic',
            field=models.CharField(blank=True, default='XXXXX-XXXXXXX-X', max_length=15, verbose_name='CNIC number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='credit_card_number',
            field=models.CharField(blank=True, max_length=24, verbose_name='Credit card number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of joining'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='User name'),
        ),
    ]
