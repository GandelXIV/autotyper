import pyautogui as pag # using this instead of kb because of linux compatibility issues
import keyboard as kb
import time
import random
import sys
import json

CONFIG_FILE = "config.txt"

def rf(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()

def parse_config(rawconfig):
    config = {}
    for line in rawconfig.split("\n"):
        try:
            key,value = line.split(":")
            config[key] = value
        except: pass
    config["speed"] = int(config["speed"])
    return config

# run
def start_typing():
    for char in text:
        codes = {
            "\n":"enter"
        }
        try: pag.press(codes[char])
        except: pag.press(char)
        wait_time = (60/config["speed"]) - press_load_time
        if wait_time > 0:
            time.sleep(wait_time)

# info
start = time.time()
pag.press("L")
press_load_time = time.time()-start
print("oad press time:", press_load_time)
print("Max typing speed: cca", round(60/press_load_time))
# init
rawconfig = rf(CONFIG_FILE)
config = parse_config(rawconfig)
text = rf(config["textfile"])
kb.add_hotkey(config['start'], start_typing)
# destruct
input("Press enter to end program...")
kb.unhook_all_hotkeys()
sys.exit()
