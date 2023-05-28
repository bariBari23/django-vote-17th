from rest_framework import serializers
from .models import *

class TeamVoteSerializer(serializers.ModelSerializer):
    team_list = (
        ('RePick', 'Repick'),
        ('바리바리', '바리바리'),
        ('Hooking', 'Hooking'),
        ('Dansupport', 'Dansupport'),
        ('TherapEse', 'TherapEse')
    )

    user = serializers.ReadOnlyField(source='user.name')
    team = serializers.ChoiceField(
        choices=team_list
    )

    class Meta:
        model = Team_Vote
        fields = ['id', 'user', 'team']