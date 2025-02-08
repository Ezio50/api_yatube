from rest_framework import serializers
from posts.models import Post, Group, Comment

class PostSerializer(serializers.ModelSerializer):
    # При выводе используем имя пользователя через slug-поле
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    # При выводе комментария отображаем автора как username
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        # Поле post делаем read-only, т.к. оно определяется из URL
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
