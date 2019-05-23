from django.contrib import admin

# Register your models here.
from .models import Profile, SemPercentage,SemMarks

admin.site.register(Profile)
admin.site.register(SemMarks)
admin.site.register(SemPercentage)


