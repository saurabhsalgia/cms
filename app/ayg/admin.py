from django.contrib import admin

# Register your models here.
from ayg.models import *


class YouthAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name'
    ]
admin.site.register(Youth, YouthAdmin)


# class FreshContactAdmin(admin.ModelAdmin):
#     list_display = [
#         'middle_name'
#     ]
# admin.site.register(FreshContact, FreshContactAdmin)


class VIPContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'referred_by',
        'follow_up_status'
    ]
admin.site.register(VIPContact, VIPContactAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'owner',
        'parent_group'
    ]
admin.site.register(Group, GroupAdmin)
