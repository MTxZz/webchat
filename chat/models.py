

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class ChatMessage ( models.Model ):
    """
    Model to represent user submitted changed to a resource guide
    """

    user = models.ForeignKey ( User, on_delete = models.CASCADE )
    group_name = models.TextField ()
    message = models.TextField ()
    created = models.DateTimeField ( auto_now_add = True )

    def __str__ (self):
        """
        String to represent the message
        """

        return self.message

    class Meta:
        verbose_name = 'chat_message'
# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.conf import settings
from django.template.defaultfilters import date as dj_date
from django.utils.translation import ugettext as _
from django.utils.timezone import localtime


class Dialog(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Dialog owner"), related_name="selfDialogs",
                              on_delete=models.CASCADE)
    opponent = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Dialog opponent"), on_delete=models.CASCADE)

    def __str__(self):
        return _("Chat with ") + self.opponent.name


class Message(TimeStampedModel, SoftDeletableModel):
    dialog = models.ForeignKey(Dialog, verbose_name=_("Dialog"), related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), related_name="messages",
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("Message text"))
    read = models.BooleanField(verbose_name=_("Read"), default=False)
    all_objects = models.Manager()

    def get_formatted_create_datetime(self):
        return dj_date(localtime(self.created), settings.DATETIME_FORMAT)

    def __str__(self):
        return self.sender.name + "(" + self.get_formatted_create_datetime() + ") - '" + self.text + "'"
