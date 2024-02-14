from django.urls import path

from blog.views import BlogListView
from mailing.apps import MailingConfig
from mailing.views import contacts, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView,\
    MessageCreateView, MailingDeleteView, MessageUpdateView, MessageDeleteView, MessageListView, MessageDetailView, \
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView


app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('blog/', BlogListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('mailing/', MailingListView.as_view(), name='list_mailing'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('message/', MessageListView.as_view(), name='list_message'),
    path('message/<int:pk>', MessageDetailView.as_view(), name='view_message'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('client/', ClientListView.as_view(), name='list_client'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
