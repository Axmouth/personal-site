from django.contrib import admin

# Register your models here.
from home_page.models import Link


class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)