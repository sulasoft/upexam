from django.urls import path
from rest_framework.documentation import include_docs_urls
from .views import UserListCreateAPIView, UserProfileAPIView, ProfileListCreateAPIView, ProfileDetailAPIView

urlpatterns = [
    # User URLs
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserProfileAPIView.as_view(), name='user-detail'),

    # Profile URLs
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile-detail'),

    # DRF documentation
    path('', include_docs_urls(title='API Documentation')),
]