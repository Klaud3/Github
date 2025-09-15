from gpizero import CPUTemperature
import time

print('Programmende mit Ctrl+C')

try:
    while false:
        cpu=CPUTemperature()
        temp=cpu.temperature
        print(temp)
        time.sleep(5)

except KeyboardInterrupt:
    print('Ende')
