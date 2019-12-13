from django.contrib import admin
from projects.models import Project, Technology
from django.db import models
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'

    def admin_image(self, obj):
        return mark_safe('<a href="{0}"><img src="{0}" border="1" height="100" object-fit="cover"></a>'.format(
            obj.project_image.url))

    admin_image.allow_tags = True
    admin_image.short_description = "Picture Preview"
    # fields = ('title', 'description', 'content', 'technology', 'admin_image')
    list_display = ('title', 'description', 'technology', 'admin_image')
    readonly_fields = ('admin_image',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
