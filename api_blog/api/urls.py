from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet


router_v1 = DefaultRouter()

router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
