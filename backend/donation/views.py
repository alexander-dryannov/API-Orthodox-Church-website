from .models import Donation
from rest_framework import generics
from .handlers import get_donation_data
from .permissions import IsStaffOrReadOnly
from .serializers import DonationSerializer


class MixinDonation:
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsStaffOrReadOnly]


class LCDonationView(MixinDonation, generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data = [value for value in get_donation_data(document[0]).values()]
            for index, field in enumerate(request.data.keys()):
                request.data[field] = data[index]
            return super().post(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)


class RUDDonationView(MixinDonation, generics.RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        if request.data.get('file'):
            document = request.data.pop('file')
            data = [value for value in get_donation_data(document[0]).values()]
            for index, field in enumerate(request.data.keys()):
                request.data[field] = data[index]
            return super().patch(request, *args, **kwargs)
        else:
            return super().patch(request, *args, **kwargs)
