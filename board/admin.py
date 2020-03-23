from django.contrib import admin
from .models import *


@admin.register(Ad)
class AdminAd(admin.ModelAdmin):
    pass


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass
