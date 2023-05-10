from django.shortcuts import render, HttpResponse
from pabrik.models import Sensor, Actuator
from django.template import loader


def main_page(request):
    sensor = Sensor.objects.all().values()
    actuator = Actuator.objects.all().values()
    template = loader.get_template('details.html')
    context = {
        'sensors': sensor,
        'actuators': actuator,
    }
    return HttpResponse(template.render(context, request))


from pabrik.MQTT import run_mqtt
run_mqtt()