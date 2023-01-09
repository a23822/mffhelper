from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "uniformName",
        "charIndex",
        "latestUniform",
        "type",
    ]

    list_filter = [
        "charIndex",
        "latestUniform",
        "type",
    ]

    search_fields = ["name"]

    list_editable = ["latestUniform"]
