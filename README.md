# beyblock20

<img src="https://raw.githubusercontent.com/ChrisChrisLoLo/beyblock20/master/images/PXL_20220821_181421951.jpg" width="500">

A 20 key modular macropad that can connect with other elements to form a larger macropad via magnets. This versatile module in combination with the encoder module (knoblin3) can be used to form a 20 key macropad with 3 encoders, a 4x10 ortholinear board, or a 4x10 ortholinear board with 3 encoders! Each module has a Seeeduino XIAO on it, and all of them communicate on an I2C bus. Because of the I2C bus, more kinds modules can be made for an even more fine tuned and customized macropad/keyboard, as well as up to 128 devices to be connected together at once!

Video demo here: https://www.youtube.com/watch?v=Z132qLr78tY

## Status
Prototyping phase. Firmware is a now working (!!!) though I will refine it to catch hotswap edgecases, as well as make the configuration process easier. I want to try to add capacitors to prevent voltage drops, as well as add some mounting holes to the knoblin3. If there's enough support for this project, I can work on adding new types of modules as well as refine the current ones. Anyone who wishes to expand on this idea are free to use the source files provided. I would produce these if you're looking to tinker and hack (and you're capable of doing so) at your own risk, though more work needs to be done before these are plug and play.

## Features
- A highly customizable framework to tailor your macropad to your needs, when you need to
  - A magnetic connector is on each side of the module, allowing you to connect the components you want, whenever you want
  - Open source, so anyone who wishes to make their own module and publish it is free to
    - Parts could include Display modules, sensors, sliders, LEDs, trackpads, etc.
    - Opens the possibility of a ecosystem of interchangible parts
- Uses hotswap sockets, so you can swap out keys to your hearts content
- Has TTRS jacks that uses the same I2C bus, so having a split keyboard should be doable!
- Aside from the magnetic connector, uses commodity parts, so it should be easy to order and assemble your own!

<img src="https://raw.githubusercontent.com/ChrisChrisLoLo/beyblock20/master/images/PXL_20220821_181439555.jpg" width="500">

## Design
This design came out the [Seeedstudio Seeeduino Xiao Keyboard Competition](https://www.seeedstudio.com/seeed-fusion-diy-xiao-mechanical-keyboard-contest.html). The Seeeduino XIAO RP2040 is a great, affordable, little microcontroller. I'm a big fan of the USB C port and castellated pins on it. It's biggest tradeoff was that there aren't as many pins on it as a pro-micro, meaning that you have to think outside the box to get enough pins to make a keyboard out of it. I found this constraint to be really fun, since I pushed me to take an I2C "split" keyboard approach. The beyblock20 also draws inspiration from Zack Freedman's [Mirage Keyboard](https://github.com/ZackFreedman/MiRage), particularly with the idea of an unbounded I2C bus.  

<img src="https://raw.githubusercontent.com/ChrisChrisLoLo/beyblock20/master/images/PXL_20220821_182140266.jpg" width="500">

Thank you to Seeedstudio for manufacturing these boards for free for the competition. I found the [Seeduino Xiao RP2040](https://www.seeedstudio.com/seeed-fusion-diy-xiao-mechanical-keyboard-contest.html) board to be an excellent product, and the community support for said board to be awesome.
<span>
<img src="https://raw.githubusercontent.com/ChrisChrisLoLo/beyblock20/master/images/PXL_20220824_113001688.jpg" width="500">
<img src="https://raw.githubusercontent.com/ChrisChrisLoLo/beyblock20/master/images/PXL_20220824_113234270.jpg" width="500">
</span>
## Parts
I will outline the main parts here, though since the design, isn't finalized, you may need a few addtional parts, like screws and such
| Part                      | Count                               | Comment                                                                                                                                                      |
|---------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seeeduino XIAO RP2040     | 1 per module                        | You can try other XIAO variants, though more parts may be required to make something like a wireless beyblock20. Any firmware written will be for the RP2040 |
| 4 pin magnetic connectors | 2 per module                        | You'll look like ones from here: https://www.adafruit.com/product/5358. I was able to get mine on AliExpress                                                 |
| M2 screws/nuts            | TBD (you'll want atleast 8 of each) | You'll need some to secure the board to the case, and the cover to the board                                                                                 |
| M2 8mm Male/Female spacer | 4                                   | Used to secure the acrylic cover to the beyblock20                                                                                                           |
| Acrylic Cover             | 1                                   | SVG in the repository. Optional                                                                                                                              |
| LL4148 SMD Diodes         | 20                                  |                                                                                                                                                              |
| Kailh Hotswap sockets     | 20                                  |    
| 0.91 inch Oled Display    | 1                                   | Optional. Typical Oled Display. NOTE: You can only have one per I2C bus, since it's not (easily) possible to have multiple displays of the same type display different things on the same I2C bus 
|3mm diameter and 2mm long neodymium magnets| 4 per module| Part of the secret sauce! This is subject to change as the case design evolves | 
