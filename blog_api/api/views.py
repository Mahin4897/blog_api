from rest_framework import viewsets, filters, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Catagory, Tag
from .serializers import (
    postSerializer,
    catagorySerializer,
    tagSerializer,
    RegisterSerializer,
)
from .permissions import IsOwnerOrAdminToEdit, IsAdminOnly
from rest_framework.response import Response


# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["catagory", "tags"]
    search_fields = ["title"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    permission_classes = [IsOwnerOrAdminToEdit]


class CatagoryViewSet(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = catagorySerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["name"]
    permission_classes = [IsAdminOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = tagSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["name"]
    permission_classes = [IsAdminOnly]
