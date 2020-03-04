from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from home_page.models import Link, TextBody


class LinkAdmin(admin.ModelAdmin):
    def admin_image(self, obj):
        return mark_safe('<a href="{0}"><img src="{0}" border="1" height="100" object-fit="cover"></a>'.format(
            obj.link_image.url))

    admin_image.allow_tags = True
    admin_image.short_description = "Picture Preview"
    list_display = ('name', 'link_target', 'admin_image')
    readonly_fields = ('admin_image',)


class TextBodyAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'


admin.site.register(Link, LinkAdmin)
admin.site.register(TextBody, TextBodyAdmin)