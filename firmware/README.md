# Firmware

## Requirements
You want to flash CircuitPython 8.0.0 or later on your boards.
For now this might even mean using the beta version.

## Installation
Run `./upload.sh bc` or `./upload.sh bp` depending on if you want to upload the beyblock20 controller (`bc`) firmware, or the beyblock20 peripheral firmware(`bp`) firmware. Running `./upload.sh kp` will now upload knoblin3 peripheral software. Windows users may need to write a cmd script that effectively copies over source files to their RP2040

## General archetecture
For the most part, this is just a few constructs built on top of KMK. This means you should get the full features of KMK.

beyblock20 works with the idea of controllers and peripherials (think I2C if you're familiar with that).

One module acts as the controller. This controller stores all the keymap information on it, so you only need to update it if you want to update your layout. In the controller keymap, you can place keys of each module you have, as well as define what modules you have. Down the road, I could likely write a helper function that stream lines the process a bit. 

All other modules are expected to be programmed as peripherals. These peripherals are pretty dumb, in that they don't store any keymap information. Instead, they report what keys got pressed when inquired by the controller. They're also capable of executing XYZ operations based on what the controller sends it (though this aspect hasn't been used yet). This means you cannot use a peripheral stand-alone. This is the trade-off for only needing to program one microcontroller for basic layout changes.

Caveats:
- You may need to explicitly define an address in some situations, espectially in the case that you're using more than 1 beyblock40 peripheral or 1 knoblin3 peripheral.
- You cannot have multiple OLEDs of the same type together, since they generally share the same I2C address.

See the source files for a better understanding
