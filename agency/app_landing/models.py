from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = FilerImageField(on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order', ]
