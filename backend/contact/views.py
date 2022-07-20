from .models import Contact
from rest_framework import generics
from .handlers import get_donation_data
from .permissions import IsStaffOrReadOnly
from .serializers import ContactSerializer


class LCContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsStaffOrReadOnly]

    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data = [value for value in get_donation_data(document[0]).values()]
            for index, field in enumerate(request.data.keys()):
                request.data[field] = data[index]
            return super().post(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)


class RUDContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsStaffOrReadOnly]

    def patch(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data = [value for value in get_donation_data(document[0]).values()]
            for index, field in enumerate(request.data.keys()):
                request.data[field] = data[index]
            return super().patch(request, *args, **kwargs)
        else:
            return super().patch(request, *args, **kwargs)
