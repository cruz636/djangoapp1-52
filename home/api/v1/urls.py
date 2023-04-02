from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ChiaViewSet,NewMoViewSet,NewMo2ViewSet,RojoViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('rojo', RojoViewSet )
router.register('newmo', NewMoViewSet )
router.register('newmo2', NewMo2ViewSet )
router.register('chia', ChiaViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
