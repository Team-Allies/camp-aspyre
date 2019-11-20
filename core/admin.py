from django.contrib import admin
from .models import User, Camper, Camp, Registration, Role

# Register your models here.

admin.site.register(User)
admin.site.register(Camper)
admin.site.register(Camp)
admin.site.register(Registration)
admin.site.register(Role)


