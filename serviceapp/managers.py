from django.db import models


class QRCodeManager(models.Manager):
    def get_queryset(self):
        return super(QRCodeManager, self).get_queryset().filter(is_active=True)