from django.contrib import admin
from tracker.models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value'] # rows in admin interface

admin.site.register(Score, ScoreAdmin) #adding models to admin interface
