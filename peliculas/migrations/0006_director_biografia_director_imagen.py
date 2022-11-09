# Generated by Django 4.0.6 on 2022-08-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0005_alter_pelicula_duracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='biografia',
            field=models.TextField(blank=True, help_text='Resumen biografia', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]