from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для работы с постами.
    Обязательное требование – использовать ModelViewSet.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # При создании автоматически записываем автора – текущего пользователя
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для работы с группами. Только операции чтения.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для комментариев, вложенный в пост.
    URL содержит параметр post_id – идентификатор поста.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        # Получаем пост через вспомогательный метод
        post = self.get_post()
        return post.comments.all()

    def get_post(self):
        """
        Надёжный способ получить пост по параметру из URL.
        Если пост не найден – выбрасываем 404.
        """
        post_id = self.kwargs.get('post_id')
        try:
            return Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise NotFound('Пост не найден.')

    def perform_create(self, serializer):
        # При создании комментария привязываем текущего пользователя и
        # пост, полученный из URL
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
