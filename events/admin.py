from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event

# Register your models here.
# admin.site.register(Venue)
admin.site.register(MyClubUser)
# admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',) # this will order the venue section in admin area in alphabatical order, if we put negative (-) in front of name, it will work in reverse orders
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)