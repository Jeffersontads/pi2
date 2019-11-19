# Generated by Django 2.2.5 on 2019-11-18 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_populate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='saborpizza',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, related_name='sabores', through='pizzas.SaborPizzaIngrediente', to='pizzas.Ingrediente'),
        ),
        migrations.AlterField(
            model_name='saborpizzaingrediente',
            name='ingrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizzas.Ingrediente'),
        ),
        migrations.AlterField(
            model_name='saborpizzaingrediente',
            name='sabor_pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.SaborPizza'),
        ),
    ]
