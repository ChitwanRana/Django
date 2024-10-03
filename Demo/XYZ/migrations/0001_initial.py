# Generated by Django 5.1.1 on 2024-09-30 17:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chaivarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('ML', 'Machine Learning'), ('DL', 'Deep Learning'), ('NLP', 'Natural Language Processing')], max_length=3)),
            ],
        ),
    ]
