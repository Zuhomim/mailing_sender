from django.urls import path

from blog.views import BlogListView
from mailing.apps import MailingConfig
from mailing.views import homepage, contacts, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MessageCreateView

app_name = MailingConfig.name

urlpatterns = [
    # path('', homepage, name='index'),
    path('', MailingCreateView.as_view(), name='list'),
    path('blog/', BlogListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('mailing/', MailingListView.as_view(), name='list_mailing'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
]