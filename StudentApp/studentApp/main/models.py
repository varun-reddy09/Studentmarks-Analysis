from django.db import models
from django.contrib.auth.models import User

class Organizer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    hall_ticket = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    current_branch = models.CharField(max_length=50)
    proctor_id = models.CharField(max_length=50)

class Marks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class ScrapyItem(models.Model):

    subject_name = models.CharField(max_length=100,null=True)

