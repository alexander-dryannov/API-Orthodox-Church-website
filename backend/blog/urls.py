from django.urls import path
from .views import LCPostView, RUDPostView


urlpatterns = [
    path('post', LCPostView.as_view(), name='list-create'),
    path('post/<int:pk>', RUDPostView.as_view(), name='retrieve-update-delete')
]
