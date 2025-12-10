import subprocess
import time

processes = []

commands = [
    "python main/manage.py runserver 8001",
    "python account/manage.py runserver 8002",
    # "python backend_comments/manage.py runserver 8003",
]

print("Backendlar ishga tushirilmoqda...\n")

for cmd in commands:
    p = subprocess.Popen(cmd, shell=True)
    processes.append(p)
    print(f"RUN: {cmd}")

print("\nBarcha backendlar ishga tushdi! CTRL + C bosib to'xtatishingiz mumkin.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTo'xtatilmoqda...")
    for p in processes:
        p.terminate()
print('x+3')