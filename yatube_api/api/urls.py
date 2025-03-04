from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet


v1_router = SimpleRouter()

v1_router.register(r'posts', PostViewSet, basename='post')
v1_router.register(r'groups', GroupViewSet, basename='group')

v1_comment_router = SimpleRouter()
v1_comment_router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
    path('v1/posts/<int:post_id>/', include(v1_comment_router.urls)),

]
