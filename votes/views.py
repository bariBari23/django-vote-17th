from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import *
# Create your views here.

class TeamVoteView(APIView):

    def get(self, request, format=None):
        vote = Team_Vote.objects.all()
        serializer = TeamVoteSerializer(vote, many=True)
        baribari = Team_Vote.objects.filter(team='바리바리').count()
        repick = Team_Vote.objects.filter(team='RePick').count()
        hooking = Team_Vote.objects.filter(team='Hooking').count()
        dansupport = Team_Vote.objects.filter(team='Dansupport').count()
        therapese = Team_Vote.objects.filter(team='TherapEse').count()
        return Response({'message': "투표 조회", '바리바리': baribari, 'RePick': repick,
                         'Hooking': hooking, 'Dansupport':dansupport,
                         'TherapEse': therapese, 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, format=None):
        user = self.request.user
        serializer=TeamVoteSerializer(data=request.data)
        if serializer.is_valid():
            if Team_Vote.objects.filter(user=user, team=serializer.validated_data['team']):
                delete_vote = Team_Vote.objects.get(user=user, team=serializer.validated_data['team'])
                delete_vote.delete()
                return Response({'message': '투표 취소', 'data': serializer.data}, status=HTTP_201_CREATED)
            else:
                serializer.save(user=self.request.user, team=serializer.validated_data['team'])
                return Response({'message':'투표 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
