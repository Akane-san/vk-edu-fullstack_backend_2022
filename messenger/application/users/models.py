from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'static/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    """Describe a user in our system."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") # noqa
    profile_pic = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0, blank=True)
    width_field = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username