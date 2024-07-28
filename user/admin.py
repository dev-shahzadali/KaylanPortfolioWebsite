from django.contrib import admin
from .models import Profile
from django.utils.html import format_html
import admin_thumbnails



class ProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;">'.format(object.profile_pic.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail','full_name', 'profession', 'description', 'email', 'number', 'linkedin', 'facebook', 'twitter', 'instagram')



admin.site.register(Profile, ProfileAdmin)
