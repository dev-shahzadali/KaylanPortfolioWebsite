from django.contrib import admin
from .models import Project, ProjectGallery
from django.utils.html import format_html
import admin_thumbnails


# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="80", height="60" >'.format(object.project_image.url))
    thumbnail.short_description = 'Project Image'
    list_display                = ('thumbnail', 'title', 'description', 'created_date', 'framework', 'view_link')
    prepopulated_fields         = {'slug': ('title',)}
    inlines                     = [ProjectGalleryInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectGallery)