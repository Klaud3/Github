from gpizero import CPUTemperature
import time

print('Programmende mit Ctrl+C')

try:
    while True:
        cpu=CPUTemperature()
        temp=cpu.temperature
        print(temp)
        time.sleep(6)

except KeyboardInterrupt:
    print('Ende')
