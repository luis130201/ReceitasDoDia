# Generated by Django 3.2.25 on 2024-12-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0007_alter_recipeitem_list_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='list_ingredient',
            field=models.ManyToManyField(to='ingredient.IngredientItem'),
        ),
    ]