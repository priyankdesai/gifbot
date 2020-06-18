A GIF bot for Raspberry Pi Zero

NOTES:

Raspberry Pi ILI 9341 Display Driver
cmake -DILI9341=ON -DGPIO_TFT_DATA_CONTROL=5 -DGPIO_TFT_RESET_PIN=6 -DGPIO_TFT_BACKLIGHT=18 -DSPI_BUS_CLOCK_DIVISOR=30 -DBACKLIGHT_CONTROL=ON -DSTATISTICS=0 ..

Run this before executing over SSH:
export DISPLAY=:0

Send command to a GUI window over SSH:
DISPLAY=:0 xdotool getactivewindow key N


