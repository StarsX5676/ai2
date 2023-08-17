import subprocess

target_ip = "38.154.242.34"  # IP server yang ingin diuji
target_port = 80  # Port yang sesuai
requests_per_second = 2000000  # Jumlah permintaan per detik
duration = 10  # Durasi pengujian dalam detik

command = "ab -n {} -c {} -g results.tsv http://{}:{}/".format(
    requests_per_second * duration, requests_per_second, target_ip, target_port
)

subprocess.call(command, shell=True)
