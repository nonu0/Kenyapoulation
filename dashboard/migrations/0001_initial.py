# Generated by Django 4.1.7 on 2023-03-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Central',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.FloatField()),
                ('density', models.FloatField()),
                ('houses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Eastern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NEastern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nyanza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RValley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Western',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=50)),
                ('area', models.FloatField(default=123.43)),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('females', models.IntegerField()),
                ('males', models.IntegerField()),
                ('total', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.county')),
            ],
        ),
    ]
