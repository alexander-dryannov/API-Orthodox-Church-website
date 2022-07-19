from django.urls import path
from .views import LCScheduleView, RUDScheduleView

urlpatterns = [
    path('schedule', LCScheduleView.as_view(), name='list-create'),
    path('schedule/<int:pk>', RUDScheduleView.as_view(), name='retrieve-update-delete')
]