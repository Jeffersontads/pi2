# Generated by Django 2.2.5 on 2019-09-13 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyzza', '0002_cliente_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SaborBordaIngredientes',
            new_name='SaborBordaIngrediente',
        ),
        migrations.RenameModel(
            old_name='SaborPizzaIngredientes',
            new_name='SaborPizzaIngrediente',
        ),
    ]