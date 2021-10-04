from threading import Thread
from time import sleep

from impulse_listener import ImpulseListener

# Define listeners
tentacle_1_serial = ImpulseListener(port=1200, tentacle_num=1)
tentacle_2_serial = ImpulseListener(port=1201, tentacle_num=2)
tentacle_3_serial = ImpulseListener(port=1202, tentacle_num=3)
tentacle_4_serial = ImpulseListener(port=1203, tentacle_num=4)
tentacle_5_serial = ImpulseListener(port=1204, tentacle_num=5)
tentacle_6_serial = ImpulseListener(port=1205, tentacle_num=6)
tentacle_7_serial = ImpulseListener(port=1206, tentacle_num=7)
tentacle_8_serial = ImpulseListener(port=1207, tentacle_num=8)

# Assign threads to start and stop listening to serial output
start_thread_1 = Thread(target=tentacle_1_serial.start_listening, name="start_listening_1")
start_thread_2 = Thread(target=tentacle_2_serial.start_listening, name="start_listening_2")
start_thread_3 = Thread(target=tentacle_3_serial.start_listening, name="start_listening_3")
start_thread_4 = Thread(target=tentacle_4_serial.start_listening, name="start_listening_4")
start_thread_5 = Thread(target=tentacle_5_serial.start_listening, name="start_listening_5")
start_thread_6 = Thread(target=tentacle_6_serial.start_listening, name="start_listening_6")
start_thread_7 = Thread(target=tentacle_7_serial.start_listening, name="start_listening_7")
start_thread_8 = Thread(target=tentacle_8_serial.start_listening, name="start_listening_8")

stop_thread_1 = Thread(target=tentacle_1_serial.stop_listening, name="stop_listening_1")
stop_thread_2 = Thread(target=tentacle_2_serial.stop_listening, name="stop_listening_2")
stop_thread_3 = Thread(target=tentacle_3_serial.stop_listening, name="stop_listening_3")
stop_thread_4 = Thread(target=tentacle_4_serial.stop_listening, name="stop_listening_4")
stop_thread_5 = Thread(target=tentacle_5_serial.stop_listening, name="stop_listening_5")
stop_thread_6 = Thread(target=tentacle_6_serial.stop_listening, name="stop_listening_6")
stop_thread_7 = Thread(target=tentacle_7_serial.stop_listening, name="stop_listening_7")
stop_thread_8 = Thread(target=tentacle_8_serial.stop_listening, name="stop_listening_8")

if __name__ == "__main__":
    # Start listening to serial output
    start_thread_1.start()
    start_thread_2.start()
    start_thread_3.start()
    start_thread_4.start()
    start_thread_5.start()
    start_thread_6.start()
    start_thread_7.start()
    start_thread_8.start()

    # Wait for 2 seconds before stopping listening to serial output
    sleep(2)
    stop_thread_1.start()
    stop_thread_2.start()
    stop_thread_3.start()
    stop_thread_4.start()
    stop_thread_5.start()
    stop_thread_6.start()
    stop_thread_7.start()
    stop_thread_8.start()