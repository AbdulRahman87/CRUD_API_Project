from django.utils.timezone import now
from django.db import models

# Create your models here.

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=255)
    note_desc = models.TextField()
    date_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.note_title