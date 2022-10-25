#from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from users.models import MyUser
# Create your models here.

class Chat(models.Model):
    class ChatType(models.TextChoices):
        DIALOG = 'DIALOG'
        CHAT = 'CHAT'
 
    chat_type = models.CharField(max_length=6, choices=ChatType.choices, verbose_name="Тип чата")
    members = models.ManyToManyField(MyUser, verbose_name="Участник")


    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", related_name="chats", on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, verbose_name="Пользователь", related_name="authors", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    pub_date = models.DateTimeField(verbose_name='Дата сообщения', default=timezone.now)
    is_readed = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        ordering=['pub_date']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return str(self.message)
