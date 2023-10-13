
from django.contrib import admin
from .models import Identification,Observation,Enquete_System,Antecedent,Exam,Diagnostique,Traitement
# Register your models here.
admin.register(Identification)
admin.register(Observation)
admin.register(Enquete_System)
admin.register(Antecedent)
admin.register(Exam)
admin.register(Diagnostique)
admin.register(Traitement)
