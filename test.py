from pythonosc import osc_message_builder
from pythonosc import udp_client
from psonic import *
import soundcard as sc
import soundfile as sf
import time
sender = udp_client.SimpleUDPClient('172.20.10.14', 4560)
while True:
    sender.send_message('/trigger/vals', [61.0, 5, 100])
    time.sleep(1)

#send_message('/trigger/prophet', [70, 100, 8])
#sender.send_message('/trigger/prophet', [70, 100, 8])

