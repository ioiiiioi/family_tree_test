from django.contrib import admin
from .models import Person, Marriage

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    autocomplete_fields = ["father", "mother", "partners"]