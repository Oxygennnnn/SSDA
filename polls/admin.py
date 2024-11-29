from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Poll, Choice, Vote

# Register your models here.
admin.site.site_header = "PollLab Admin"
admin.site.site_title = "PollLab Admin Area"
admin.site.index_title = "Welcome to the PollLab Admin"

class ChoiceInline(admin.TabularInline):
    model = Choice

class PollAdmin(admin.ModelAdmin):
    fields = ['text', 'pub_date', 'poll_id','active']
    list_display = ('text', 'pub_date', 'poll_id', 'active')
    inlines = [ChoiceInline]

# Register the models
admin.site.register(Poll, PollAdmin)
admin.site.unregister(Group)
