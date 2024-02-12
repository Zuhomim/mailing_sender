from django.contrib import admin

from mailing.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'periodicity', 'status',)
    search_fields = ('time', 'periodicity', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)
