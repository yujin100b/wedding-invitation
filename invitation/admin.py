from django.contrib import admin
from .models import Letter, Attendance, Cheering, Funding, Subscriber

from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Letter)
class LetterrAdmin(ImportExportModelAdmin):
    list_display = ('code', 'target', 'relation', 'lang', 'invitee', 'message', 'name', 'honor', 'full_name', 'phone', 'email', )

@admin.register(Attendance)
class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'attend_yn', 'method', 'name', 'phone', 'email', 'bgm', 'get_paper_invitation', 'junior_name', 'attend_time', 'offline_camera_yn', 'created_date',)

@admin.register(Cheering)
class CheeringAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'cheer_message', 'created_date', )

@admin.register(Funding)
class FundingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'amount', 'how_to_spend', 'address', 'payment', 'created_date', )


@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'where_to_regist', )