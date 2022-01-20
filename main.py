from Henon import henon
from Tinker import PRESET_1, Configuration, tinker
from Zaslavskii import PRESET, zas

hr = henon(1, 1, points=500)
CONFIG = PRESET_1
CONFIG.points = 1000
tk = tinker(PRESET_1)
PRESET.points = 1000
zs = zas(PRESET)
#PRESET.graph = False
#ZS = iterateGrid(20, PRESET)
