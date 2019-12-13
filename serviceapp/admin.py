from django.contrib import admin
from .models import QRCode, QRZone, Feedback

# Register your models here.
admin.site.register(Feedback)
admin.site.register(QRCode)
admin.site.register(QRZone)