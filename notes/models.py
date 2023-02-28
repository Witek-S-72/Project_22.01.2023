from django.db import models

# Create your models here

STATUS = (('opublikowane','published'), ('nieopublikowane','unpublished'), ('w redakcji','pending'))

class Note(models.Model):
    """klasa reprezentuje notatkę"""
    status = models.CharField(max_length=40, default='enter status', choices=STATUS)
    title = models.CharField(max_length=30)
    note = models.TextField()
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f'{self.title}, {self.creation_datetime}'

    class Meta:
        verbose_name = 'Notatka'
        verbose_name_plural = 'Notatki'

