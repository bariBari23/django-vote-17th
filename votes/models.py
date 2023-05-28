from django.db import models

from accounts.models import User


# Create your models here.

class Team_Vote(models.Model):
    team_list = (
        ('RePick', 'RePick'),
        ('바리바리', '바리바리'),
        ('Hooking', 'Hooking'),
        ('Dansupport', 'Dansupport'),
        ('TherapEse', 'TherapEse')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    team = models.CharField(max_length=16, choices=team_list)

    def __str__(self):
        return f'{self.user.name} : {self.team}'
