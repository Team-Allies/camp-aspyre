from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Camper, Camp, Registration, Role, MedicalInformation

class CampAdmin(admin.ModelAdmin):
    list_display = (
    'name_of_camp',
    'camp_start_date',
    'camp_end_date',
    'camp_location_street_address',
    'camp_location_city',
    'number_of_campers',
    )

admin.site.register(User, UserAdmin)
admin.site.register(Camper)
admin.site.register(Camp, CampAdmin)
admin.site.register(Registration)
admin.site.register(Role)
admin.site.register(MedicalInformation)




