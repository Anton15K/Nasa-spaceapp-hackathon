from pythonosc import osc_message_builder
from pythonosc import udp_client
from psonic import *
import time
sender = udp_client.SimpleUDPClient('172.20.10.14', 4560)
#send_message('/trigger/prophet', [70, 100, 8])
#sender.send_message('/trigger/prophet', [70, 100, 8])
while True:
    sender.send_message('/trigger/vals', [40.0, 100, 530])
    time.sleep(1)