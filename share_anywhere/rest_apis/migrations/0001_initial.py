# Generated by Django 5.1.4 on 2024-12-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_text', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent')], default='pending', max_length=20)),
            ],
        ),
    ]
