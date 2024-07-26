from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/post', PostViewSet, 'post')
router.register('api/comment', CommentViewSet, 'comment')

urlpatterns = router.urls