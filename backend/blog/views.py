from .models import Post
from .handlers import convert_image
from rest_framework import generics
from .serializers import PostSerializer
from .permissions import IsStaffOrReadOnly


class LCPostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsStaffOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['cover'] = convert_image(
            request.data['cover'], field_name='cover')
        return super().post(request, *args, **kwargs)


class RUDPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsStaffOrReadOnly]

    def patch(self, request, *args, **kwargs):
        if request.data.get('cover'):
            request.data['cover'] = convert_image(
                request.data['cover'], field_name='cover')
            return super().patch(request, *args, **kwargs)
        else:
            return super().patch(request, *args, **kwargs)
