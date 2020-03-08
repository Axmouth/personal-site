from django.db import models


# Create your models here.
from django.utils.translation import ugettext_lazy


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ugettext_lazy("Category")
        verbose_name_plural = ugettext_lazy("Categories")


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    is_published = models.BooleanField(default=False)
    sub_url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_url_base():
        return '/blog/post/'

    def get_url(self):
        return self.get_url_base() + str(self.sub_url) + '/'

    def get_absolute_url(self):
        return self.get_url()

    class Meta:
        verbose_name = ugettext_lazy("Blog Post")
        verbose_name_plural = ugettext_lazy("Blog Posts")
