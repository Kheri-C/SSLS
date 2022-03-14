# Kheri Chavira A01658773
# Ramiro Rosas A01376780
# Marco Palacios A01650354
# Gonzalo Romero A01656942

"""
Para ejecutar este código, es necesario conectar 4 micrófonos 
a la computadora y colocar el ID correcto de cada micrófono en las
líneas 14, 15, 16 y 17.

Este código solo obtiene la potencia de las 4 grabaciones que realiza.
"""
# IDs de los micrófonos
device_index1 = 6
device_index2 = 7
# device_index3 = 6
# device_index4 = 7

import pyaudio
import simpleaudio as sa
import wave
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import signal

WAVE_OUTPUT_FILENAME1 = "audio1.wav"
WAVE_OUTPUT_FILENAME2 = "audio2.wav"
# WAVE_OUTPUT_FILENAME3 = "audio3.wav"
# WAVE_OUTPUT_FILENAME4 = "audio4.wav"

##################################################
#                 GRABAR AUDIO                   #
##################################################

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

# Mostrar los ID de los micrófonos
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print ("Input id {0} - {1}".format(i, p.get_device_info_by_host_api_device_index(0, i).get('name')))

start = time.time()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Tiempo de la grabación por micrófono
RECORD_SECONDS = 1

for i in range(1,11):
 
    audio = pyaudio.PyAudio()
    
    # Comienza a grabar
    stream1 = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, input_device_index = device_index1,
                    frames_per_buffer=CHUNK)

    stream2 = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, input_device_index = device_index2,
                    frames_per_buffer=CHUNK)

    # stream3 = audio.open(format=FORMAT, channels=CHANNELS,
    #                 rate=RATE, input=True, input_device_index = device_index3,
    #                 frames_per_buffer=CHUNK)

    # stream4 = audio.open(format=FORMAT, channels=CHANNELS,
    #                 rate=RATE, input=True, input_device_index = device_index4,
    #                 frames_per_buffer=CHUNK)

    print("grabando...")

    frames1 = []
    frames2 = []
    # frames3 = []
    # frames4 = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        
        data1 = stream1.read(CHUNK, exception_on_overflow = False)
        frames1.append(data1)

        data2 = stream2.read(CHUNK, exception_on_overflow = False)
        frames2.append(data2)

        # data3 = stream3.read(CHUNK, exception_on_overflow = False)
        # frames3.append(data3)

        # data4 = stream4.read(CHUNK, exception_on_overflow = False)
        # frames4.append(data4)

    print("grabación termina")
    
    # Termina de grabar
    stream1.stop_stream()
    stream2.stop_stream()
    # stream3.stop_stream()
    # stream4.stop_stream()

    stream1.close()
    stream2.close()
    # stream3.close()
    # stream4.close()

    audio.terminate()
    
    waveFile = wave.open(WAVE_OUTPUT_FILENAME1, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames1))
    waveFile.close()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME2, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames2))
    waveFile.close()

    # waveFile = wave.open(WAVE_OUTPUT_FILENAME3, 'wb')
    # waveFile.setnchannels(CHANNELS)
    # waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    # waveFile.setframerate(RATE)
    # waveFile.writeframes(b''.join(frames3))
    # waveFile.close()

    # waveFile = wave.open(WAVE_OUTPUT_FILENAME4, 'wb')
    # waveFile.setnchannels(CHANNELS)
    # waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    # waveFile.setframerate(RATE)
    # waveFile.writeframes(b''.join(frames4))
    # waveFile.close()

    ##################################################
    #         EXTRAER AUDIO DE LOS ARCHIVOS          #
    ##################################################

    spf1 = wave.open(WAVE_OUTPUT_FILENAME1, "r")
    spf2 = wave.open(WAVE_OUTPUT_FILENAME2, "r")
    # spf3 = wave.open(WAVE_OUTPUT_FILENAME3, "r")
    # spf4 = wave.open(WAVE_OUTPUT_FILENAME4, "r")

    # Extraer aduio de los archivos .wav
    signal1 = spf1.readframes(-1)
    signal1 = np.fromstring(signal1, "Int16")
    signal2 = spf2.readframes(-1)
    signal2 = np.fromstring(signal2, "Int16")
    # signal3 = spf3.readframes(-1)
    # signal3 = np.fromstring(signal3, "Int16")
    # signal4 = spf4.readframes(-1)
    # signal4 = np.fromstring(signal4, "Int16")


    ##################################################
    #              OBTENER LA POTENCIA               #
    ##################################################

    power1 = np.mean(signal1**2)
    power2 = np.mean(signal2**2)
    # power3 = np.mean(signal3**2)
    # power4 = np.mean(signal4**2)

    print("Potencia L: {0}".format(abs(1/power1)))
    print("Potencia R: {0}".format(abs(1/power2)))
    # print("Potencia 3: {0}".format(1/power3))
    # print("Potencia 4: {0}".format(1/power4))

    end = time.time()

    print("Tiempo de ejecución: {0}".format(str(end - start)))