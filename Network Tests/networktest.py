import os
import sys

t = 0

if(len(sys.argv) > 1 and str(sys.argv[1]) == 'c'):
    print('Cleaning File')
    networktests = open('networktests.txt', 'w')
    networktests.write('Overwritten File\n')
    networktests.close()

networktests = open('networktests.txt', 'a')
networktests.write('Start of Trial\n')
networktests.close()

ipaddress = input('input ip address: ')

while(t < 3):
    os.system('ping ' + str(ipaddress) + ' >> networktests.txt')
    t += 1
    print('End of Trial ' + str(t))

networktests = open('networktests.txt', 'a')
networktests.write('End of Trial\n')

networktests.close()