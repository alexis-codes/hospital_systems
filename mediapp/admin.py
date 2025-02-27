from django.contrib import admin
from mediapp.models import *


# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(staff)
admin.site.register(ward)

