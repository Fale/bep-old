from django.contrib import admin
from wheel.models import Wheel, Sector

class WheelAdmin(admin.ModelAdmin):
    fields =  ['name']

admin.site.register(Wheel)
admin.site.register(Sector)
