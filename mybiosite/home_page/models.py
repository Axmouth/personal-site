from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy


class Link(models.Model):
    name = models.CharField(max_length=20)
    link_target = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ugettext_lazy("Link")
        verbose_name_plural = ugettext_lazy("Links")