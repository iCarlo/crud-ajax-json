from django.contrib import admin

from .models import CrudUser


@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'age')
    list_filter = ('address', 'age')
    search_fields = ('name',)
