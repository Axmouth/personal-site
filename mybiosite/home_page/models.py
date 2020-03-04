from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy


class Link(models.Model):
    name = models.CharField(max_length=20)
    link_target = models.CharField(max_length=150)
    link_image = models.ImageField(upload_to='documents/%Y/%m/%d/',  default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ugettext_lazy("Link")
        verbose_name_plural = ugettext_lazy("Links")


class TextBody(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ugettext_lazy("Text Body")
        verbose_name_plural = ugettext_lazy("Text Bodies")