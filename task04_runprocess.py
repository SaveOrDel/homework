import sys
import subprocess

print(f"run: {' '.join(sys.argv[1:])}")

try:
    subprocess.run(sys.argv[1:])
except FileNotFoundError:
    print(f"Не найден запускаемый файл: {sys.argv[1]}")
except Exception as e:
    print(f"Other error: {e}")
