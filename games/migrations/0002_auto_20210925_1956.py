# Generated by Django 3.2.7 on 2021-09-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='game_name',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description of Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Name of game'),
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(null=True, related_name='category', to='games.Category'),
        ),
    ]
