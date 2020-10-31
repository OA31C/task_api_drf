from rest_framework.authtoken.models import Token
from ..posts.models import Post, Comment, Vote
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer user"""

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Redesigned and create method for password hashing"""

        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""

    comments = serializers.StringRelatedField(many=True)
    creation_date = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True
    )

    class Meta:
        model = Post
        fields = ["title", "link", "creation_date", "count_votes", "author", "comments"]


class CommentSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S", required=False, read_only=True
    )

    class Meta:
        model = Comment
        fields = ["post", "author", "content", "creation_date"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["user", "post", "like"]
