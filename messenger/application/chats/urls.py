"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from chats.views import chat_list, chat_create, chat_detail, chat_delete, chat_add_member,\
                        messages_list, message_create, message_detail, message_delete,\
                        message_edit, custom_handler405

handler405 = custom_handler405

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<chat_id>/messages/', messages_list, name='messages_list'),

    path('create/', chat_create, name='chat_create'),
    path('<chat_id>/create/', message_create, name='message_create'),

    path('<chat_id>/', chat_detail, name='chat_detail'),
    path('messages/<message_id>', message_detail, name='message_detail'),

    path('<chat_id>/delete/', chat_delete, name='chat_delete'),
    path('messages/<message_id>/delete/', message_delete, name='message_delete'),

    path('<chat_id>/add_member/', chat_add_member, name='chat_add_member'),
    path('messages/<message_id>/edit/', message_edit, name='message_edit'),
]
