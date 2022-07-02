from django.urls import path, include
from .views import PostViewsSet, UserViewsSet #DetailPost, ListPost, UserList, UserDetail, 
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users', UserViewsSet, basename='users')
router.register('', PostViewsSet, basename='posts')

urlpatterns = router.urls


# urlpatterns = [
#     path('', ListPost.as_view()),
#     path('<int:pk>/', DetailPost.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]

