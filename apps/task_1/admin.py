from django.contrib import admin
from apps.task_1.models import People, Document


class AdminPeople(admin.ModelAdmin):
    list_display = ('name',)


class AdminDocument(admin.ModelAdmin):
    list_display = ('education',)

admin.site.register(People, AdminPeople)
admin.site.register(Document, AdminDocument)
