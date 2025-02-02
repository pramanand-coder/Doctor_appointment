from django.contrib import admin
from .models import patient_info, doctor_infos, scheduled_appointments

# List of models to register
models = [patient_info, doctor_infos, scheduled_appointments]

# Register each model in the admin site
for model in models:
    admin.site.register(model)
