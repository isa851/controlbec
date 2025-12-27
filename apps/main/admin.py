from apps.main.models import SiteInfo
from django.contrib import admin

# Register your models here.
@admin.register(SiteInfo)
class SiteInfo(admin.ModelAdmin):
    list_display = ["title","description"]