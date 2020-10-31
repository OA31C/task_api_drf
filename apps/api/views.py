from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.models import Token
from ..posts.models import Post, Comment, Vote
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response(
                {"error": "Please provide both username and password"},
                status=HTTP_400_BAD_REQUEST,
            )
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, url_path="upvote", methods=["post"])
    def upvote(self, request, pk, *args, **kwargs):
        url = str(request)
        post_id = int(url.split("posts/")[-1].split("/upvote/'>")[0])
        post = get_object_or_404(Post, id=post_id)
        Vote.objects.create(user=request.user, post=post, value=1)
        return Response({"message": f"Your like post {post.title}"})


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
