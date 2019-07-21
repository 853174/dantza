# Generated by Django 2.2.1 on 2019-05-31 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mota', models.CharField(max_length=100)),
                ('egoera', models.CharField(max_length=100)),
                ('deskribapena', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dantzaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=50)),
                ('abizenak', models.CharField(max_length=200)),
                ('jaiotze_data', models.DateTimeField(verbose_name='jaiotze data')),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Materiala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mota', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tresna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_mota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dantza.Materiala')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zenbakia', models.IntegerField()),
                ('dantzari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dantza.Dantzaria')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialArduraduna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haste_data', models.DateTimeField(verbose_name='haste data')),
                ('oharrak', models.CharField(max_length=200)),
                ('dantzari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dantza.Dantzaria')),
            ],
        ),
        migrations.CreateModel(
            name='Mailegua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailegatze_data', models.DateTimeField(verbose_name='mailegatze data')),
                ('itzulita', models.BooleanField(default=False)),
                ('arropa', models.ManyToManyField(to='dantza.Arropa')),
                ('dantzari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dantza.Dantzaria')),
                ('materiala', models.ManyToManyField(to='dantza.Tresna')),
            ],
        ),
        migrations.CreateModel(
            name='ArropaArduraduna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haste_data', models.DateTimeField(verbose_name='haste data')),
                ('oharrak', models.CharField(max_length=200)),
                ('dantzari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dantza.Dantzaria')),
            ],
        ),
    ]
