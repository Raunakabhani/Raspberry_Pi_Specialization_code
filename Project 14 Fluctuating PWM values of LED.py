from gpiozero import PWMLED
from time import sleep

# Create a PWMLED instance named 'led' on GPIO pin 14
led = PWMLED(14)

# Set the LED to full brightness (1) for 1 second
led.value = 1
sleep(1)

# Set the LED to half-brightness (0.5) for 1 second
led.value = 0.5
sleep(1)

# Turn off the LED (0) for 1 second
led.value = 0
sleep(1)

try:
    # Continuously fade the LED in and out
    while True:
        # Fade in
        for duty_cycle in range(0, 100, 1):
            led.value = duty_cycle / 100.0
            sleep(0.05)

        # Fade out
        for duty_cycle in range(100, 0, -1):
            led.value = duty_cycle / 100.0
            sleep(0.05)

except KeyboardInterrupt:
    # Handle program interruption
    print("Program stopped; turning off the LED")
    led.value = 0
    pass
