# Generated by Django 5.2.1 on 2025-05-30 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('provider', models.ForeignKey(limit_choices_to={'user_type': 'ProviderProvider'}, on_delete=django.db.models.deletion.CASCADE, related_name='bookings_received', to=settings.AUTH_USER_MODEL)),
                ('seeker', models.ForeignKey(limit_choices_to={'user_type': 'SeekerSeeker'}, on_delete=django.db.models.deletion.CASCADE, related_name='bookings_made', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='services.servicelisting')),
            ],
        ),
    ]
