from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserSignupSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['id', 'username','password','name', 'created_at', 'updated_at', 'part', 'team']

    part_list = (
        ('프론트엔드', '프론트엔드'),
        ('백엔드', '백엔드')
    )

    team_list = (
        ('RePick', 'Repick'),
        ('바리바리', '바리바리'),
        ('Hooking', 'Hooking'),
        ('Dansupport', 'Dansupport'),
        ('TherapEse', 'TherapEse')
    )

    username = serializers.CharField(max_length=32) # 아이디
    password = serializers.CharField(max_length=32)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=8) # 이름
    part = serializers.ChoiceField(
        choices=part_list
    )
    team = serializers.ChoiceField(
        choices=team_list
    )

    def create(self, validated_data):

        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError('username 존재')
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError('email 존재')

        else:
            user = User.objects.create(
                username=validated_data['username'],
                name=validated_data['name'],
                email=validated_data['email'],
                part=validated_data['part'],
                team=validated_data['team']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user