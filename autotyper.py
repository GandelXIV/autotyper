print("Loading...")
import pyautogui as pag # using this instead of kb because of linux compatibility issues
import keyboard as kb
import time
import random
import sys
import json

codes = {
            "\n":"enter",
            # need czech keyboard
            "ř":["+", "r"],
            "ě":["+","e"],
            "š":["+","s"],
            "č":["+","c"],
            "ž":["+","z"],
            "ý":["=","y"],
            "á":["=","a"],
            "í":["=","i"],
            "é":["=","e"],
            "ď":["+","d"],
            "é":["=","e"],
            "ň":["+","n"],
            "ó":["=","o"],
            "ú":["=","u"],
            "ť":["+","t"],
            "ů":";",
            "Ř":["+", "R"],
            "Ě":["+","E"],
            "Š":["+","S"],
            "Č":["+","C"],
            "Ž":["+","Z"],
            "Ý":["=","Y"],
            "Á":["=","A"],
            "Í":["=","I"],
            "É":["=","E"],
            "Ď":["+","D"],
            "É":["=","E"],
            "Ň":["+","N"],
            "Ó":["=","O"],
            "Ú":["=","U"],
            "Ť":["+","T"],
            "Ů":";",
}

CONFIG_FILE = "config.txt"

def error(msg):
    raise BaseException(msg)

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

def apply_random(text):
    a = list(text)
    for i in range(int(config["mistakes"])):
        a.insert(random.randrange(0, len(text)), "§")
    newtext = ''
    for e in a:
        newtext += e
    return newtext

# run
def start_typing():
    for char in text:
        if char == "§":
            try: pag.press(codes[random.choice(config["mistake-keys"])])
            except: pag.press(random.choice(config["mistake-keys"]))
            pag.press("backspace")
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
try: rawconfig = rf(CONFIG_FILE)
except: error("Missing config.txt!")
try: config = parse_config(rawconfig)
except: error("Invalid config.txt!")
try: text = rf(config["textfile"])
except: error("Could not find text file!")
if "mistakes" in config:
    text = apply_random(text)
kb.add_hotkey(config['start'], start_typing)
# destruct
input("Press enter to end program...")
kb.unhook_all_hotkeys()
sys.exit()
