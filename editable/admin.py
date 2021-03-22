from django.contrib import admin
from models import Placeholder

class PlaceholderAdmin(admin.ModelAdmin):
	list_display = ('location', 'content')

admin.site.register(Placeholder, PlaceholderAdmin)

