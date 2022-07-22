from .models import Post
from rest_framework import generics
from .serializers import PostSerializer
from .permissions import IsStaffOrReadOnly


class MixinBlog:
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsStaffOrReadOnly]


class LCPostView(MixinBlog, generics.ListCreateAPIView):
    pass


class RUDPostView(MixinBlog, generics.RetrieveUpdateDestroyAPIView):
    pass
