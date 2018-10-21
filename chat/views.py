

from django.contrib.auth.decorators import login_required


@login_required
def chatList(request):
    pass
    return render(request, 'privateChat/chatList.html')



import uuid

from django.shortcuts import render

from .models import ChatMessage


# Create your views here.

@login_required
def index(request):
    pass
    return render(request, 'index.html')


def rooms(request):
    #uid4 = str(uuid.uuid4())
    return render(request, 'chatRoom/rooms.html')


def chatRoom(request, room_name):
    chat_messages = ChatMessage.objects.filter(group_name=room_name).order_by("created")[:100]
    return render(request, 'chatRoom/chatRoom.html', {
        'chat_messages': chat_messages,
        'room_name': room_name
    })

from django.views import generic
from braces.views import LoginRequiredMixin

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from . import models
from . import utils
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q


class DialogListView(LoginRequiredMixin, generic.ListView):
    template_name = 'privateChat/dialogs.html'
    model = models.Dialog
    ordering = 'modified'

    def get_queryset(self):
        dialogs = models.Dialog.objects.filter(Q(owner=self.request.user) | Q(opponent=self.request.user))
        return dialogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.kwargs.get('username'):
            # TODO: show alert that user is not found instead of 404
            user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
            dialog = utils.get_dialogs_with_user(self.request.user, user)
            if len(dialog) == 0:
                dialog = models.Dialog.objects.create(owner=self.request.user, opponent=user)
            else:
                dialog = dialog[0]
            context['active_dialog'] = dialog
        else:
            context['active_dialog'] = self.object_list[0]
        if self.request.user == context['active_dialog'].owner:
            context['opponent_username'] = context['active_dialog'].opponent.username
        else:
            context['opponent_username'] = context['active_dialog'].owner.username
        context['ws_server_path'] = '{}://{}:{}/'.format(
            settings.CHAT_WS_SERVER_PROTOCOL,
            settings.CHAT_WS_SERVER_HOST,
            settings.CHAT_WS_SERVER_PORT,
        )
        return context
