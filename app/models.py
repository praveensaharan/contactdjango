import email
from sqlite3 import Timestamp
from unicodedata import name
from django.db import models
GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    roll = models.CharField(max_length=20, default='SOME STRING')
    phone = models.CharField(max_length=10, default='SOME STRING')
    GENDER_CHOICES = (('Mumbai-Delhi', 'Mumbai-Delhi '), ('Mumbai-Chennai',
                      'Mumbai-Chennai'), ('Chennai-Kolkata', 'Chennai-Kolkata'))
    dropdown = models.CharField(
        max_length=15, choices=GENDER_CHOICES, default='SOME STRING')
    # public = models.BooleanField(default=True)

    subject = models.TextField()
    # Timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
