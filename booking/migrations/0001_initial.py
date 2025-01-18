# Generated by Django 5.1.5 on 2025-01-18 00:12

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('date', models.DateField()),
                ('time_slot', models.IntegerField(choices=[(12, '12:00 - 13:00'), (13, '13:00 - 14:00'), (14, '14:00 - 15:00'), (15, '15:00 - 16:00'), (16, '16:00 - 17:00'), (17, '17:00 - 18:00'), (18, '18:00 - 19:00'), (19, '19:00 - 20:00'), (20, '20:00 - 21:00'), (21, '21:00 - 22:00'), (22, '22:00 - 23:00')])),
                ('guests', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(12)])),
                ('booking_notes', models.TextField()),
                ('allergies', models.ManyToManyField(blank=True, to='booking.allergen')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
