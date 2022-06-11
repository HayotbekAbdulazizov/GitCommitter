from django.contrib import admin
from .models import GitProfile, Repository


@admin.register(GitProfile)
class GitProfileAdmin(admin.ModelAdmin):
	list_display = ['username', 'pat', 'full_name','email','password','description']
	list_display_links = ['username', 'pat', 'full_name','email','password','description']

@admin.register(Repository)
class TagAdmin(admin.ModelAdmin):
	list_display = ['profile', 'name', 'id']
	list_display_links = ['profile', 'name', 'id']
	# prepopulated_fields = {'slug':('name',)}

