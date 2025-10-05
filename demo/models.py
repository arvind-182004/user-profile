from django.db import models

class Profile(models.Model):
    name = models.CharField()
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    address = models.TextField(max_length=256)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.name
