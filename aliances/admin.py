from django.contrib import admin
from .models import Aliance


@admin.register(Aliance)
class AlianceAdmin(admin.ModelAdmin):

    list_display = [
        "name",
    ]

    search_fields = ["name"]
