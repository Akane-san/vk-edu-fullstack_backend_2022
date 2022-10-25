from django.core import serializers
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render, redirect

from chats.models import Message, Chat
from users.models import MyUser

# Create your views here.
def custom_handler405(request, exception):
    # Call when Http404 raised
    return HttpResponseNotAllowed('Этот метод запрещён!')

def index(request):
    return render(request, "chats/index.html")

def chat_list(request): #✔
    if request.method == "GET":
        chats = Chat.objects.all()
        chats_list = serializers.serialize('json', chats)
        return HttpResponse(chats_list, content_type="text/json-comment-filtered")
    return HttpResponse(status=405)

def chat_create(request): #✔
    if request.method == "POST":
        chat = Chat.objects.create(chat_type=request.GET.get('chat_type'))
        members = request.GET.getlist('members')
        for member in members:
            try:
                user = MyUser.objects.get(id=member)
                chat.members.add(user)
            except MyUser.DoesNotExist:
                return HttpResponseNotFound("Нет такого пользователя")
        chat.save()
    return HttpResponse(status=405)

def chat_detail(request, chat_id): #✔
    if request.method == "GET":
        try:
            chat = Chat.objects.get(id=chat_id)
            chat_serialized = serializers.serialize('json', chat)
            return HttpResponse(chat_serialized, content_type="text/json-comment-filtered")
        except Chat.DoesNotExist:
            return HttpResponseNotFound("Нет такого чата")
    return HttpResponse(status=405)

def chat_delete(request, chat_id): #✔
    if request.method == "DELETE":
        try:
            chat = Chat.objects.get(id=chat_id)
            chat.delete()
        except Chat.DoesNotExist:
            return HttpResponseNotFound("Нет такого чата")
    return HttpResponse(status=405)

def chat_add_member(request, chat_id):
    if request.method == "POST":
        try:
            chat_obj = Chat.objects.get(id=chat_id)
            member_id = request.GET.get('member')
            member = MyUser.objects.get(id=member_id)
            if chat_obj.members.len>1 and chat_obj.chat_type == "DIALOG":
                chat_obj.chat_type = "CHAT"
            chat_obj.members.add(member)
            chat_obj.save()
        except Chat.DoesNotExist:
            return HttpResponseNotFound("Нет такого чата")
        except MyUser.DoesNotExist:
            return HttpResponseNotFound("Нет такого пользователя")
    return HttpResponse(status=405)

def messages_list(request, chat_id): #✔
    if request.method == "GET":
        messages = Message.objects.get(chat=chat_id)
        messages_list = serializers.serialize('json', messages)
        return HttpResponse(messages_list, content_type="text/json-comment-filtered")
    return HttpResponse(status=405)

def message_create(request, chat_id): #✔
    if request.method == "POST":
        author = request.GET.get('author')
        message = request.GET.get('message_type')
        message = Message.objects.create(chat = chat_id, author = author, message= message)
        message.save()
    return HttpResponse(status=405)

def message_detail(request, message_id): #✔
    if request.method == "GET":
        message = Message.objects.get(id=message_id)
        message_serialized = serializers.serialize('json', message)
        return HttpResponse(message_serialized, content_type="text/json-comment-filtered")
    return HttpResponse(status=405)

def message_delete(request, message_id): #✔
    if request.method == "DELETE":
        message = Message.objects.get(id=message_id)
        message.delete()
    return HttpResponse(status=405)

def message_edit(request, message_id): #✔
    if request.method == "POST":
        message_obj = Message.objects.get(id=message_id)
        message = request.GET.get('message', message_obj.message)
        is_readed = request.GET.get('is_readed', message_obj.is_readed)
        message_obj.message = message
        message_obj.is_readed = is_readed
        message_obj.save()
    return HttpResponse(status=405)