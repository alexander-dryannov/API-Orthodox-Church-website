from django.urls import path
from .views import LCDonationView, RUDDonationView


urlpatterns = [
    path('donation', LCDonationView.as_view(), name='list-create'),
    path('donation/<int:pk>', RUDDonationView.as_view(), name='retrieve-update-delete')
]
