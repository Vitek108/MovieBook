# Generated by Django 3.2.7 on 2021-10-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200)),
                ('rezie', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zanr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_zanru', models.CharField(max_length=80)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviebook.film')),
            ],
        ),
    ]