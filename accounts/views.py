from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny


# Create your views here.

class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '회원가입 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSignupSerializer(users, many=True)
        return Response({'message': '유저 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


#로그인 함수
class LoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSignupSerializer(user)
        return Response({'message': '현재 로그인된 유저 정보 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=HTTP_200_OK)


