from django.contrib import admin
from .models import Letter, Attendance, Cheering, Funding, Subscriber

@admin.register(Letter)
class LetterrAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Cheering)
class CheeringAdmin(admin.ModelAdmin):
    pass

@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass