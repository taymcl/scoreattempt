from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Register your models here.
admin.site.register(Profile)


class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class AccountUserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, AccountUserAdmin)
