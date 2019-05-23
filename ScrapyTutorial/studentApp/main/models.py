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
    proctor_id =  models.CharField(max_length=50)

class SemMarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject_name = models.CharField(max_length=100)
    int1_maxMarks = models.FloatField(default=0)
    int1_secMarks = models.FloatField(default=0)
    int2_maxMarks = models.FloatField(default=0)
    int2_secMarks = models.FloatField(default=0)
    ass1_maxMarks = models.FloatField(default=0)
    ass1_secMarks = models.FloatField(default=0)
    ass2_maxMarks = models.FloatField(default=0)
    ass2_secMarks = models.FloatField(default=0)
    ass3_maxMarks = models.FloatField(default=0)
    ass3_secMarks = models.FloatField(default=0)
    quiz1_maxMarks = models.FloatField(default=0)
    quiz1_secMarks = models.FloatField(default=0)
    quiz2_maxMarks = models.FloatField(default=0)
    quiz2_secMarks = models.FloatField(default=0)
    quiz3_maxMarks = models.FloatField(default=0)
    quiz3_secMarks = models.FloatField(default=0)
    sessional_maxMarks = models.FloatField(default=0)
    sessional_secMarks = models.FloatField(default=0)
    External_grade = models.CharField(max_length=10,default = "-")

class SemPercentage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    int1_percentage = models.FloatField(default=0)
    int2_percentage = models.FloatField(default=0)
    ass1_percentage = models.FloatField(default=0)
    ass2_percentage = models.FloatField(default=0)
    ass3_percentage = models.FloatField(default=0)
    quiz1_percentage = models.FloatField(default=0)
    quiz2_percentage = models.FloatField(default=0)
    quiz3_percentage = models.FloatField(default=0)
    sessional_pecentage = models.FloatField(default=0)
    SGPA = models.FloatField(default=0)







