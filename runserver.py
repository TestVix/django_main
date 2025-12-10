import subprocess
import time
import signal
import os

processes = []
# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.main.settings")

PYTHON = r".\venv\Scripts\python.exe"

commands = [
    ['python', 'main/manage.py', 'runserver', '8001'],
    # [PYTHON, "-m", "uvicorn", "main.main.asgi:application", "--reload", "--port", "8001"],
    [PYTHON, "-m", "uvicorn", "fast_api_account.main:app", "--reload", "--port", "8002"],
]

print("Backendlar ishga tushirilmoqda...\n")

for cmd in commands:
    p = subprocess.Popen(cmd)
    processes.append(p)
    print(f"RUN: {' '.join(cmd)}")

print("\nBarcha backendlar ishga tushdi! CTRL + C bosib to'xtatishingiz mumkin.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTo‘xtatilmoqda...")
    for p in processes:
        p.send_signal(signal.SIGTERM)
