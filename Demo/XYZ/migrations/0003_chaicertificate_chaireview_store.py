# Generated by Django 5.1.1 on 2024-10-03 17:06

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XYZ', '0002_chaivarity_desc_alter_chaivarity_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('chai', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='XYZ.chaivarity')),
            ],
        ),
        migrations.CreateModel(
            name='ChaiReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='XYZ.chaivarity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('chai_varieties', models.ManyToManyField(related_name='store', to='XYZ.chaivarity')),
            ],
        ),
    ]
