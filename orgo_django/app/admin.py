from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.SingleStepProblem)
admin.site.register(models.PredictProductsProblem)

