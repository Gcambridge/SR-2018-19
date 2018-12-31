import os

t = 0

networktests = open("networktests.txt", "a")
networktests.write("<trial>")
networktests.close()

while(t < 3):
    os.system('ping 192.168.4.1 >> networktests.txt')
    t += 1
    print(t)

networktests = open("networktests.txt", "a")
networktests.write("</trial>")
networktests.close()