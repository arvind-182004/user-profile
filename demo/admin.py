from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile
        fields = ['name','email','mobile']

admin.site.register(Profile,ProfileAdmin)
