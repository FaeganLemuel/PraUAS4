from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import ActuatorSerializer, SensorSerializer
from .models import Actuator, Sensor


def kandang_temperatur(client, userdata, msg):
    object_ = Sensor.objects.get(name="kandang/temperatur")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def kandang_kelembaban(client, userdata, msg):
    object_ = Sensor.objects.get(name="kandang/kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def kandang_pakan(client, userdata, msg):
    object_ = Sensor.objects.get(name="kandang/pakan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def wagyu_berat(client, userdata, msg):
    object_ = Sensor.objects.get(name="wagyu/berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def wagyu_kualitas(client, userdata, msg):
    object_ = Sensor.objects.get(name="wagyu/kualitas")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))



def wagyu_lemak(client, userdata, msg):
    object_ = Sensor.objects.get(name="wagyu/lemak")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def ikan_berat(client, userdata, msg):
    object_ = Sensor.objects.get(name="ikan/berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def ikan_lemak(client, userdata, msg):
    object_ = Sensor.objects.get(name="ikan/lemak")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def ikan_panjang(client, userdata, msg):
    object_ = Sensor.objects.get(name="ikan/panjang")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def beras_berat(client, userdata, msg):
    object_ = Sensor.objects.get(name="beras/berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def beras_aroma(client, userdata, msg):
    object_ = Sensor.objects.get(name="beras/aroma")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def beras_air(client, userdata, msg):
    object_ = Sensor.objects.get(name="beras/air")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def sayur_berat(client, userdata, msg):
    object_ = Sensor.objects.get(name="sayur/berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def sayur_warna(client, userdata, msg):
    object_ = Sensor.objects.get(name="sayur/warna")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def sayur_keasaman(client, userdata, msg):
    object_ = Sensor.objects.get(name="sayur/keasaman")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def buah_berat(client, userdata, msg):
    object_ = Sensor.objects.get(name="buah/berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def buah_warna(client, userdata, msg):
    object_ = Sensor.objects.get(name="buah/warna")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def buah_keasaman(client, userdata, msg):
    object_ = Sensor.objects.get(name="buah/keasaman")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def musim_angin(client, userdata, msg):
    object_ = Sensor.objects.get(name="musim/angin")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def musim_suhu(client, userdata, msg):
    object_ = Sensor.objects.get(name="musim/suhu")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def musim_kelembaban(client, userdata, msg):
    object_ = Sensor.objects.get(name="musim/kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def jual_makanan(client, userdata, msg):
    object_ = Sensor.objects.get(name="jual/makanan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def jual_minuman(client, userdata, msg):
    object_ = Sensor.objects.get(name="jual/minuman")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def jual_service(client, userdata, msg):
    object_ = Sensor.objects.get(name="jual/service")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def pengunjung_kepuasan(client, userdata, msg):
    object_ = Sensor.objects.get(name="pengunjung/kepuasan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def pengunjung_jumlah(client, userdata, msg):
    object_ = Sensor.objects.get(name="pengunjung/jumlah")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def pengunjung_promosi(client, userdata, msg):
    object_ = Sensor.objects.get(name="pengunjung/promosi")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(object_, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('recieved data ', msg.payload.decode('utf-8'))


def run_mqtt():
    client = mqtt.Client("DjangoApp")
#farm
    client.message_callback_add("farm/kandang/temperatur", kandang_temperatur)
    client.message_callback_add("farm/kandang/kelembaban", kandang_kelembaban)
    client.message_callback_add("farm/kandang/pakan", kandang_pakan)

    client.message_callback_add("farm/wagyu/berat", wagyu_berat)
    client.message_callback_add("farm/wagyu/kualitas", wagyu_kualitas)
    client.message_callback_add("farm/wagyu/lemak", wagyu_lemak)

    client.message_callback_add("farm/ikan/berat", ikan_berat)
    client.message_callback_add("farm/ikan/lemak", ikan_lemak)
    client.message_callback_add("farm/ikan/panjang", ikan_panjang)
#plantation
    client.message_callback_add("plantation/beras/berat", beras_berat)
    client.message_callback_add("plantation/beras/aroma", beras_aroma)
    client.message_callback_add("plantation/beras/air", beras_air)

    client.message_callback_add("plantation/sayur/berat", sayur_berat)
    client.message_callback_add("plantation/sayur/warna", sayur_warna)
    client.message_callback_add("plantation/sayur/keasaman", sayur_keasaman)

    client.message_callback_add("plantation/buah/berat", buah_berat)
    client.message_callback_add("plantation/buah/warna", buah_warna)
    client.message_callback_add("plantation/buah/keasaman", buah_keasaman)
#restaurant
    client.message_callback_add("restaurant/musim/angin", musim_angin)
    client.message_callback_add("restaurant/musim/suhu", musim_suhu)
    client.message_callback_add("restaurant/musim/kelembaban", musim_kelembaban)

    client.message_callback_add("restaurant/jual/makanan", jual_makanan)
    client.message_callback_add("restaurant/jual/minuman", jual_minuman)
    client.message_callback_add("restaurant/jual/service", jual_service)

    client.message_callback_add("restaurant/pengunjung/kepuasan", pengunjung_kepuasan)
    client.message_callback_add("restaurant/pengunjung/jumlah", pengunjung_jumlah)
    client.message_callback_add("restaurant/pengunjung/promosi", pengunjung_promosi)

    client.connect('localhost', 1883)
    client.loop_start()
#farm
    client.subscribe("farm/kandang/temperatur")
    client.subscribe("farm/kandang/kelembaban")
    client.subscribe("farm/kandang/pakan")

    client.subscribe("farm/wagyu/berat")
    client.subscribe("farm/wagyu/kualitas")
    client.subscribe("farm/wagyu/lemak")

    client.subscribe("farm/ikan/berat")
    client.subscribe("farm/ikan/lemak")
    client.subscribe("farm/ikan/panjang")
#plantation
    client.subscribe("plantation/beras/berat")
    client.subscribe("plantation/beras/aroma")
    client.subscribe("plantation/beras/air")

    client.subscribe("plantation/sayur/berat")
    client.subscribe("plantation/sayur/warna")
    client.subscribe("plantation/sayur/keasaman")

    client.subscribe("plantation/buah/berat")
    client.subscribe("plantation/buah/warna")
    client.subscribe("plantation/buah/keasaman")
#restaurant
    client.subscribe("restaurant/musim/angin")
    client.subscribe("restaurant/musim/suhu")
    client.subscribe("restaurant/musim/kelembaban")

    client.subscribe("restaurant/jual/makanan")
    client.subscribe("restaurant/jual/minuman")
    client.subscribe("restaurant/jual/service")

    client.subscribe("restaurant/pengunjung/kepuasan")
    client.subscribe("restaurant/pengunjung/jumlah")
    client.subscribe("restaurant/pengunjung/promosi")
