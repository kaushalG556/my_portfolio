from django.contrib import admin
from .models import Skill,Project, Experience, ContactMessage,Certification

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(ContactMessage)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'duration')

admin.site.register(Certification, CertificationAdmin)