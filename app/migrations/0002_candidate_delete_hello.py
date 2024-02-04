# Generated by Django 4.2.3 on 2023-11-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=3000)),
                ('skills', models.TextField(max_length=3000)),
                ('degree', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('experience', models.TextField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
    ]
