from django.contrib import admin
from .models import person,areas_affected,address_search


admin.site.register(person)
admin.site.register(areas_affected)
admin.site.register(address_search)

