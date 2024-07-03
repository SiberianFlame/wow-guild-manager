from django.db import models
from wgm_app_auth.models import UserProfile


def profile_avatar_directory_path(instance: 'UserProfile', filename):
    """
    Creating path for profile avatar image
    :param instance: Profile object
    :param filename: Name of the file
    :return: Path string
    """

    return 'avatar/{0}/{1}'.format(instance.user.profile.nickname, filename)


class Guild(models.Model):
    guildmaster = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='guild')
    name = models.CharField(max_lenght=30, verbose_name='name')
    description = models.TextField(max_lenght=256, verbose_name='description', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time and date')
    avatar = models.ImageField(upload_to=profile_avatar_directory_path,
                               null=True,
                               blank=True,
                               verbose_name='avatar',
                               default='avatar/def.png')
