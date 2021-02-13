from django.contrib import admin
from .models import virus_record, mail_info, asset
# Register your models here.


class virus_recordAdmin(admin.ModelAdmin):
    list_display = ['id', 'pcip', 'username',
                    'status', 'number', 'handle_time']


class mail_infoAdmin(admin.ModelAdmin):
    list_display = ['username', 'usermail']


class assetAdmin(admin.ModelAdmin):
    list_display = ['Requisition_date', 'Materials', 'Department',
                    'Requisitioner', 'Requisition_Num', 'Requisition_purpose', 'Purchaser']


admin.site.register(virus_record, virus_recordAdmin)
admin.site.register(mail_info, mail_infoAdmin)
admin.site.register(asset, assetAdmin)
