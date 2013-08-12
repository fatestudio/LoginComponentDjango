from django.contrib import admin
from cssa_web.models import User
from cssa_web.models import Album
from cssa_web.models import Photo
from cssa_web.models import Event
from cssa_web.models import File

class UserAdmin(admin.ModelAdmin):
#    date_hierarchy = 'pub_date'
#    ordering = ['last_name']
    list_display = ('first_name', 'last_name', 'ucsb_email')
       
admin.site.register(User, UserAdmin)
#admin.site.register(Album, AuthorAdmin)
#admin.site.register(Photo, AuthorAdmin)
#admin.site.register(Event, AuthorAdmin)
#admin.site.register(File, AuthorAdmin)
