from .models import Schedule
from .handlers import get_data
from django.http import JsonResponse
from .permissions import IsStaffOrReadOnly
from rest_framework import status, generics
from .serializers import ScheduleSerializer


class MixinSchedule:
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsStaffOrReadOnly]


class LCScheduleView(MixinSchedule, generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            if request.data.get('title'):
                document = request.data.pop('file')
                data = get_data(document[0])
                request.data['data'] = data
                return super().create(request, *args, **kwargs)
            else:
                return JsonResponse(
                    {
                        'status_code': status.HTTP_204_NO_CONTENT,
                        'message': 'Не указано название.'
                    },
                    json_dumps_params={'ensure_ascii': False}
                )
        except AttributeError:
            return JsonResponse(
                {
                    'status_code': status.HTTP_204_NO_CONTENT,
                    'message': 'Файл не был выбран.'
                },
                json_dumps_params={'ensure_ascii': False})


class RUDScheduleView(MixinSchedule, generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data = get_data(document[0])
            request.data['data'] = data
            return super().partial_update(request, *args, **kwargs)
        else:
            return super().partial_update(request, *args, **kwargs)
