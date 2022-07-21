from .models import Cleric
from django.http import JsonResponse
from .handlers import get_cleric_data
from .serializers import ClericSerializer
from .permissions import IsStaffOrReadOnly
from rest_framework import status, generics


class MixinClergy:
    queryset = Cleric.objects.all()
    serializer_class = ClericSerializer
    permission_classes = [IsStaffOrReadOnly]


class LCClericView(MixinClergy, generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            document = request.data.pop('file')
        except AttributeError:
            return JsonResponse(
                {
                    'status_code': status.HTTP_204_NO_CONTENT,
                    'message': 'Файл не был выбран.'
                },
                json_dumps_params={'ensure_ascii': False})
        if request.data.get('name'):
            data, photo = get_cleric_data(document[0])
            request.data['data'] = data
            if photo is not None:
                request.data['photo'] = photo
            return super().create(request, *args, **kwargs)
        else:
            return JsonResponse(
                {
                    'status_code': status.HTTP_204_NO_CONTENT,
                    'message': 'Не указано имя.'
                },
                json_dumps_params={'ensure_ascii': False}
            )


class RUDClericView(MixinClergy, generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data, photo = get_cleric_data(document[0])
            request.data['photo'] = photo
            request.data['data'] = data
            return super().partial_update(request, *args, **kwargs)
        else:
            return super().partial_update(request, *args, **kwargs)
