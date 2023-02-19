from django.urls import path

from smart_home.measurement.views import info_sensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('info_sensor/', info_sensor),
]
