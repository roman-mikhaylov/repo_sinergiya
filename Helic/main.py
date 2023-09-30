# 🚁 ☁️ 🌩️ 🟩 🌲 🛢️ 🌊 🏥 🧡 ⚙️⬜
from clouds_ import Clouds
from map import Map
import time
import os
from helicopter import Helicopter as Helic
from pynput import keyboard
import json

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 75
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helic = Helic(MAP_W, MAP_H)
tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def process_key(key):
    global helic, tick, clouds, field
    c = key.char.lower()
    # движение вертолёта
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helic.move(dx, dy)
    # сохранение
    if c == 'q':
        data = {"helicopter": helic.export_data(),
                "clouds": clouds.export_data(),
                "field": field.export_data(),
                "tick": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # восстановление
    elif c == 'z':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helic.import_data(data["helicopter"])
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])
            tick = data["tick"] or 1





listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()        



while True:
    os.system("cls")
    field.process_helicopter(helic, clouds)
    helic.print_menu()
    field.print_map(helic, clouds)
    print("TICK", tick)
    tick +=1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generation_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()         


