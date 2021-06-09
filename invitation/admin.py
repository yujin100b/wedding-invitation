from django.contrib import admin
from .models import Attendance, Cheering, Funding, Subscriber

from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Attendance)
class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'method', 'name', 'phone', 'email', 'attend_time', 'offline_camera_yn', 'created_date',)

@admin.register(Cheering)
class CheeringAdmin(ImportExportModelAdmin):
    list_display = ('id', 'cheer_message', 'created_date', )

@admin.register(Funding)
class FundingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'amount', 'how_to_spend', 'address', 'payment', 'created_date', )

@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id', 'email', 'where_to_regist', )