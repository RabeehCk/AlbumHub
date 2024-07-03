from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()

router.register("albums",views.AlbumViewsetView,basename="albums")


urlpatterns = [

    path("register/",views.UserRegisterView.as_view(),name='register'),

    path("token/",ObtainAuthToken.as_view()),

    path("tracks/<int:pk>/",views.TrackViewSetView.as_view(),name="tracks"),

    path("reviews/<int:pk>/",views.ReviewViewsetView.as_view(),name="reviews"),

    path("review_mixin/<int:pk>/",views.ReviewMixinView.as_view(),name="review_mixin"),

]+router.urls