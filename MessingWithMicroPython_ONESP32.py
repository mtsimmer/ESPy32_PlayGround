#SUPER lazy micro python
import machine
import utime

GREEN = machine.Pin(16, machine.Pin.OUT)
GREEN.value(0)
GREEN.value(1)
GREEN.off()
GREEN.on()
YELLOW = machine.Pin(2, machine.Pin.OUT)
YELLOW.value(0)
YELLOW.value(1)
YELLOW.off()
YELLOW.on()
RED = machine.Pin(12, machine.Pin.OUT)
RED.value(0)
RED.value(1)
RED.off()
RED.on()

for i in range(3):
	GREEN.off()
	YELLOW.off()
	RED.off()
	RED.on()
	utime.sleep(1)
	RED.off()
	YELLOW.on()
	utime.sleep(0.3)
	YELLOW.off()
	GREEN.on()
	utime.sleep(0.8)
	GREEN.off()

Analog_Pin = machine.Pin(0,machine.Pin.IN)
Analog_Light = machine.ADC(machine.Pin(36))
Analog_Light.read()


if Analog_Light.read() < 4095:
	GREEN.off()
	YELLOW.off()
	RED.off()