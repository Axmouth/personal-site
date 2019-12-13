from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        full_path = [self.name]
        # k = self.parent
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(default="")
    technology = models.CharField(max_length=20)
    project_image = models.ImageField(upload_to='documents/%Y/%m/%d/', default='pic_folder/None/no-img.jpg')
    technologies_used = models.ManyToManyField('Technology', related_name='projects')
    is_published = models.BooleanField(default=False)
    sub_url = models.CharField(max_length=100, unique=True)

    @staticmethod
    def get_url_base(self):
        return '/projects/detail/'

    def get_url(self):
        return self.get_url_base() + str(self.sub_url) + '/'
