from django.db import models

# Create your models here.

GENDER_CHOICES = (('Mr.','Mr.'), ('Mrs.','Mrs.'), ('unknown','pending'))

class PersonalData(models.Model):
    """klasa reprezentujaca danych osobowych uzytkowanika"""
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Mr.')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'Position: {self.id}, {self.gender}, {self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'



