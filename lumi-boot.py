import time
import sys
import os

def anim_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

anim_print("cpu...")
time.sleep(1)
os.system("lscpu -e=CPU,MHZ")
anim_print("ram...")
time.sleep(1)
os.system("free --mega")
anim_print("launching compiler...")
time.sleep(1)
os.system("python3 luminarka.py")

