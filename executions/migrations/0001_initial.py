# Generated by Django 4.2.1 on 2023-05-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('sales', models.IntegerField(default=0)),
            ],
        ),
    ]