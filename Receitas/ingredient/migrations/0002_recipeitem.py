# Generated by Django 2.1 on 2019-06-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('img_url', models.TextField()),
                ('list_ingredient', models.ManyToManyField(to='ingredient.ingredientItem')),
            ],
        ),
    ]
