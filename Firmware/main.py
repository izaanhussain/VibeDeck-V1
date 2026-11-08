
import board
import busio
import random
import displayio
import terminalio
import i2cdisplaybus  # circuitpython 9+, use 'displayio.I2CDisplay' if 8
import adafruit_displayio_ssd1306
from adafruit_display_text import label

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules import Module
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D6, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((board.D8, board.D9, board.D10, False),)
encoder.divisor = 4  


oled_w, oled_h = 128, 32


cats = [
    (r" /\_/\ ", "( o.o )", r" > ^ <", "meow"),
    (r" /\_/\ ", "( -.- )", r" > ^ <", "zzz"),
    (r" /\_/\ ", "( ^.^ )", r"  (u u)", "purr"),
    (r" /\_/\ ", "( O.O )", r" > o <", "!!"),
    (r" /\_/\ ", "( >w< )", r"  =^.^=", "mrow"),
]


class CatScreen(Module):
    
    def __init__(self):
        self.last = -1
        self.text = None

    def during_bootup(self, keyboard):
        displayio.release_displays()
        i2c = busio.I2C(board.SCL, board.SDA)
        bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
        display = adafruit_displayio_ssd1306.SSD1306(bus, width=oled_w, height=oled_h)

        self.text = label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            line_spacing=1.0,
            anchor_point=(0.5, 0.5),
            anchored_position=(oled_w // 2, oled_h // 2),
        )
        group = displayio.Group()
        group.append(self.text)
        display.root_group = group
        self.show_cat()

    def show_cat(self):
       
        i = random.randrange(len(cats))
        while i == self.last:
            i = random.randrange(len(cats))
        self.last = i
        self.text.text = "\n".join(cats[i])

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if is_pressed:
            self.show_cat()
        return key

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return


keyboard.modules.append(CatScreen())


copy = KC.LCTRL(KC.C)
paste = KC.LCTRL(KC.V)
undo = KC.LCTRL(KC.Z)
redo = KC.LCTRL(KC.Y)
zoom_out = KC.LCTRL(KC.MINUS)
zoom_in = KC.LCTRL(KC.EQUAL)
screenshot = KC.LGUI(KC.LSHIFT(KC.S))  # win+shift+s snipping tool
mute = KC.MUTE  # speaker mute/unmute
mic = KC.LALT(KC.A)  # zoom mic toggle.


keyboard.keymap = [
    [
        copy, paste, undo,
        redo, zoom_out, zoom_in,
        mute, mic, screenshot,
    ]
]


encoder.map = [
    ((KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.MPLY),)
]

if __name__ == "__main__":
    keyboard.go()