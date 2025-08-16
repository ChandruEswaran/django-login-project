from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
    qualification = models.TextField()
    experience = models.IntegerField(null=True, blank=True)
    about_you = models.TextField(blank=True)

    def __str__(self):
        return self.name