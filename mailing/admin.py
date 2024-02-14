from django.contrib import admin

from mailing.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_date', 'end_date', 'periodicity', 'status',)
    search_fields = ('start_date', 'end_date', 'periodicity', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)
