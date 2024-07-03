from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from account import views

router = DefaultRouter()
#
# router.register(r'users/favorite',
#                 views.FavoriteArticlesViewSet,
#                 basename='favorite-articles')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include("djoser.social.urls")),
]
