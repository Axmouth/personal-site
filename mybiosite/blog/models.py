from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        full_path = [self.name]
        # k = self.parent
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    is_published = models.BooleanField(default=False)
    sub_url = models.CharField(max_length=100, unique=True)

    @staticmethod
    def get_url_base(self):
        return '/blog/post/'

    def get_url(self):
        return self.get_url_base() + str(self.sub_url) + '/'
