from django.contrib import admin
#from django.contrib.auth.models import User

# Register your models here.
from chats.models import Chat, Message
from users.models import MyUser

class ChatAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class MyUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MyUser, MyUserAdmin)