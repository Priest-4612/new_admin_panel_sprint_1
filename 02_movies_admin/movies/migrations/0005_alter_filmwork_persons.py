# Generated by Django 3.2 on 2022-04-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_filmwork_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person', verbose_name='persons'),
        ),
    ]
