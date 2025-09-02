from django.urls import path, include
from .views import PostViewSet, CatagoryViewSet, TagViewSet, RegisterView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"catagories", CatagoryViewSet, basename="catagory")
router.register(r"tags", TagViewSet, basename="tag")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
]
