from django.contrib import admin
from .models import GitProfile, Repository
from django.contrib import admin






class RepositoryInline(admin.TabularInline):
    model = Repository




@admin.register(GitProfile)
class GitProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']
    list_display_links = ['username', 'id']
    inlines = [RepositoryInline,]



@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ['profile', 'name']
    list_display_links = ['profile', 'name']


# admin.site.register(GitProfile)
# admin.site.register(Repository)