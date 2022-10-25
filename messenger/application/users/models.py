from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'static/user_{0}/{1}'.format(instance.user.id, filename)

class MyUser(AbstractUser):
    profile_pic = models.ImageField(
        verbose_name='Иконка пользователя',
        upload_to=user_directory_path,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(verbose_name='Высота иконки', default=0, blank=True)
    width_field = models.IntegerField(verbose_name='Ширина иконки', default=0, blank=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.username