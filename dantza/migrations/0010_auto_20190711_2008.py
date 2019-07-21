# Generated by Django 2.2.2 on 2019-07-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dantza', '0009_ekitaldia_dantzariak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dantza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('deskr', models.CharField(blank=True, max_length=200)),
                ('iraupena', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='ekitaldia',
            name='dantzak',
            field=models.ManyToManyField(blank=True, to='dantza.Dantza'),
        ),
    ]
