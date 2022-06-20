from django.urls import path, include
from .views import DetailPost, ListPost
urlpatterns = [
    path('', ListPost.as_view()),
    path('<int:pk>/', DetailPost.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

