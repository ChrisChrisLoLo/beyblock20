print("Starting")

from kb import KMKKeyboard
from kmk.keys import KC
from i2c_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.cg_swap import CgSwap
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

oled_ext = Oled(
    keyboard.i2c,
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False
    )

media = MediaKeys()

keyboard.extensions = [oled_ext, media]

layers_ext = Layers()
cg_swap = CgSwap()
modtap = ModTap()
mouse_keys = MouseKeys()

keyboard.modules = [layers_ext, cg_swap, modtap, mouse_keys, tapdance]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = 1
RAISE = 2
LOWER_RAISE = 3

keyboard.keymap = [
    [
        KC.Q,KC.W,KC.E,KC.R,KC.T,
        KC.A,KC.S,KC.D,KC.F,KC.G,
        KC.Z,KC.X,KC.C,KC.V,KC.B,
        KC.ESC,KC.LGUI,XXXXXXX,KC.MT(KC.TAB, KC.LCTRL),KC.LT(LOWER, KC.SPACE),

        KC.Y,KC.U,KC.I,KC.O,KC.P,
        KC.H,KC.J,KC.K,KC.L,KC.SCOLON,
        KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,
        KC.MO(RAISE),KC.MT(KC.BSPC, KC.LSHIFT, prefer_hold=False),XXXXXXX,KC.LALT,KC.ENTER,

        KC.MS_LEFT,KC.MS_RIGHT,
        KC.MW_UP,KC.MW_DOWN,
        KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,
    ],
    [
        KC.EXCLAIM,KC.AT,KC.HASH,KC.DOLLAR,KC.PERCENT,
        KC.TILDE,KC.UNDERSCORE,KC.PLUS,KC.LEFT_CURLY_BRACE,KC.RIGHT_CURLY_BRACE,
        KC.PIPE,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,

        KC.CIRCUMFLEX,KC.AMPERSAND,KC.ASTERISK,KC.LEFT_PAREN,KC.RIGHT_PAREN,
        KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.DOUBLE_QUOTE,
        _______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
    [
        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.GRAVE,KC.MINUS,KC.EQUAL,KC.LBRACKET,KC.RBRACKET,
        KC.BSLASH,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,

        KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,
        KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.QUOTE,
        _______,_______,_______,_______,_______,
        _______,_______,_______,_______,_______,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
    [
        KC.RESET,_______,_______,_______,_______,
        KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
        KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,
        _______,_______,_______,_______,_______,

        _______,_______,_______,_______,KC.DEL,
        KC.F6,KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP,_______,_______,
        KC.F12,_______,_______,_______,_______,
        _______,KC.CG_SWAP,_______,KC.CG_SWAP,_______,

        _______,_______,
        _______,_______,
        _______,_______,
    ],
]

if __name__ == '__main__':
    keyboard.go()