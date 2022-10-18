from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class Chat(models.Model):
    class ChatType(models.TextChoices):
        DIALOG = 'DIALOG'
        CHAT = 'CHAT'
 
    chat_type = models.CharField(max_length=6, choices=ChatType.choices)
    members = models.ManyToManyField(User, verbose_name="Участник")


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь",  on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    pub_date = models.DateTimeField(verbose_name='Дата сообщения', default=timezone.now)
    is_readed = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        ordering=['pub_date']

    def __str__(self):
        return str(self.message)
