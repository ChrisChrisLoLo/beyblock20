print("Starting")

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules import tapdance
from kmk.modules.cg_swap import CgSwap
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.rapidfire import RapidFire

TAP_TIME = 300

keyboard = KMKKeyboard()

keyboard.debug_enabled = True

# oled_ext = Oled(
#     keyboard.i2c,
#     OledData(
#         corner_one={0:OledReactionType.STATIC,1:["layer"]},
#         corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
#         corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
#         corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
#     ),
#     toDisplay=OledDisplayMode.TXT,
#     flip=False
#     )

# init_display(keyboard.i2c)

media = MediaKeys()

# keyboard.extensions = [oled_ext, media]
keyboard.extensions = [media]


layers_ext = Layers()
cg_swap = CgSwap()
modtap = ModTap()
mouse_keys = MouseKeys()
rapid_fire = RapidFire()
tap_dance = TapDance()
tap_dance.tap_time = 150

modtap.tap_time = TAP_TIME

keyboard.modules = [layers_ext, cg_swap, modtap, mouse_keys, rapid_fire, tap_dance]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO


STANDARD = 0
# layer where GUI is swapped.
# We use this instead of the GUI swap feature
# as the swap doesn't seem to work with ModTap
GUI_SWAP = 1 

LOWER = 2
RAISE = 3

# TODO: look into KMK bug where pressing KC.LT(XX) and then pressing KC.MO(XX) breaks everything
LOWER_RAISE = 4


keyboard.keymap = [
    [   
        # left half
        KC.Q,KC.W,KC.E,KC.R,KC.T,
        KC.A,KC.S,KC.D,KC.F,KC.G,
        KC.Z,KC.X,KC.C,KC.V,KC.B,
        KC.LT(LOWER_RAISE, KC.ESC, tap_time=TAP_TIME),KC.LGUI,KC.MT(KC.TAB, KC.LCTRL, tap_interrupted=True),KC.MO(LOWER),KC.SPACE,
        
        # right half
        KC.Y,KC.U,KC.I,KC.O,KC.P,
        KC.H,KC.J,KC.K,KC.L,KC.SCOLON,
        KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,
        KC.MO(RAISE),KC.MT(KC.BSPC, KC.LSHIFT),XXXXXXX,KC.LALT,KC.ENTER,

        # encoders
        KC.MS_LEFT,KC.MS_RIGHT,
        KC.MW_UP,KC.MW_DOWN,
        KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,
    ],
    [
        KC.Q,KC.W,KC.E,KC.R,KC.T,
        KC.A,KC.S,KC.D,KC.F,KC.G,
        KC.Z,KC.X,KC.C,KC.V,KC.B,
        KC.LT(LOWER_RAISE, KC.ESC, tap_time=TAP_TIME),KC.LCTRL,XXXXXXX,KC.MT(KC.TAB, KC.LGUI, tap_interrupted=True),KC.LT(LOWER, KC.SPACE, tap_interrupted=True),

        KC.Y,KC.U,KC.I,KC.O,KC.P,
        KC.H,KC.J,KC.K,KC.L,KC.SCOLON,
        KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,
        KC.MO(RAISE),KC.TD(KC.MT(KC.BSPC, KC.LSHIFT), KC.BSPC),XXXXXXX,KC.LALT,KC.ENTER,

        KC.MS_LEFT,KC.MS_RIGHT,
        KC.MW_UP,KC.MW_DOWN,
        KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,
    ],
    [
        KC.EXCLAIM,KC.AT,KC.HASH,KC.DOLLAR,KC.PERCENT,
        KC.TILDE,KC.UNDERSCORE,KC.PLUS,KC.LEFT_CURLY_BRACE,KC.RIGHT_CURLY_BRACE,
        KC.PIPE,_______,_______,_______,_______,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,

        KC.CIRCUMFLEX,KC.AMPERSAND,KC.ASTERISK,KC.LEFT_PAREN,KC.RIGHT_PAREN,
        KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.DOUBLE_QUOTE,
        _______,_______,_______,_______,_______,
        KC.MO(LOWER_RAISE),XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
    [
        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.GRAVE,KC.MINUS,KC.EQUAL,KC.LBRACKET,KC.RBRACKET,
        KC.BSLASH,_______,_______,_______,_______,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,KC.MO(LOWER_RAISE),

        KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,
        KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.QUOTE,
        _______,_______,_______,_______,_______,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
    [
        KC.RESET,_______,_______,_______,_______,
        KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
        KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,
        XXXXXXX,KC.DF(GUI_SWAP),XXXXXXX,KC.DF(STANDARD),XXXXXXX,

        _______,_______,_______,_______,KC.DEL,
        KC.F6,KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,_______,_______,
        KC.F12,_______,_______,_______,_______,
        XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,XXXXXXX,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
]

if __name__ == '__main__':
    keyboard.go()