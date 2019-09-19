# Generated by Django 2.2.4 on 2019-09-18 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyzza', '0003_auto_20190913_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tamanhopizza',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='tamanhopizza',
            name='valor_adicional',
        ),
        migrations.AddField(
            model_name='saborpizza',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
