from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

comment_router = SimpleRouter()
comment_router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [

    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),

]
