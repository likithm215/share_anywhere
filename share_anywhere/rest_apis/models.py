from django.db import models


class Command(models.Model):
    command_text = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('sent', 'Sent')], default='pending')

    def __str__(self):
        return self.command_text

