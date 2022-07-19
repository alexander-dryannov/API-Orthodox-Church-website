from django.urls import path
from .views import LCClericView, RUDClericView

urlpatterns = [
    path('cleric', LCClericView.as_view(), name='list-create'),
    path('cleric/<int:pk>', RUDClericView.as_view(), name='retrieve-update-delete')
]
