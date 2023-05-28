from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from .models import *
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import *
from django.db.models import Count
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


class PartVoteView(APIView):
    def get(self, request, format=None):
        vote = Part_Vote.objects.all()
        serializer = PartVoteSerializer(vote, many=True)
        vote_count = Part_Vote.objects.filter().values('part').annotate(total=Count('part')).order_by('-total')
        return Response({'message': "투표 조회", 'vote_count':vote_count, 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, format=None):
        user = self.request.user
        serializer=PartVoteSerializer(data=request.data)
        if serializer.is_valid():
            if Part_Vote.objects.filter(user=user, part=serializer.validated_data['part']):
                delete_vote = Part_Vote.objects.get(user=user, part=serializer.validated_data['part'])
                delete_vote.delete()
                return Response({'message': '투표 취소', 'data': serializer.data}, status=HTTP_201_CREATED)
            else:
                serializer.save(user=self.request.user, part=serializer.validated_data['part'])
                return Response({'message':'투표 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


