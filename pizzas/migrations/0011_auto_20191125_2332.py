# Generated by Django 2.2.5 on 2019-11-26 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0010_auto_20191123_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamanhopizza',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipopizza',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]