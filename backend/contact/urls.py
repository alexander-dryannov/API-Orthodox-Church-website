from django.urls import path
from .views import LCContactView, RUDContactView


urlpatterns = [
    path('contact', LCContactView.as_view(), name='list-create'),
    path('contact/<int:pk>', RUDContactView.as_view(), name='retrieve-update-delete')
]
