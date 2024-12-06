from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Poll, Choice, Vote
from django.forms import widgets

# Register your models here.
admin.site.site_header = "Polling System Admin"
admin.site.site_title = "Polling System Admin Area"
admin.site.index_title = "Welcome to the Polling System Admin"

class ChoiceInline(admin.TabularInline):
    model = Choice

class PollAdmin(admin.ModelAdmin):
    fields = ['owner', 'text', 'pub_date', 'poll_id','active']
    list_display = ('text', 'pub_date', 'poll_id', 'active', "owner")
    inlines = [ChoiceInline]

    def formfield_for_dbfield(self, db_field, request, **kwargs):
            if db_field.name == "poll_id":
                kwargs['widget'] = widgets.TextInput(attrs={'placeholder': 'Generate automatically'})
            return super().formfield_for_dbfield(db_field, request, **kwargs)

# Register the models
admin.site.register(Poll, PollAdmin)
admin.site.unregister(Group)
