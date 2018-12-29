#!/usr/bin/python
# -*- coding: utf-8 -*-
'''''''''''''''''''''''''''''''' ' ' ' '''''''''''''''''''''''''''''''''''''''''

    ▄▄▄▄    ▄▄▄       █     █░ ██▓      ██████ ▓█████  ▄████▄
    ▓█████▄ ▒████▄    ▓█░ █ ░█░▓██▒    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█
    ▒██▒ ▄██▒██  ▀█▄  ▒█░ █ ░█ ▒██░    ░ ▓██▄   ▒███   ▒▓█    ▄
    ▒██░█▀  ░██▄▄▄▄██ ░█░ █ ░█ ▒██░      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
    ░▓█  ▀█▓ ▓█   ▓██▒░░██▒██▓ ░██████▒▒██████▒▒░▒████▒▒ ▓███▀ ░
    ░▒▓███▀▒ ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
    ▒░▒   ░   ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░░ ░▒  ░ ░ ░ ░  ░  ░  ▒
    ░    ░   ░   ▒     ░   ░    ░ ░   ░  ░  ░     ░   ░
    ░            ░  ░    ░        ░  ░      ░     ░  ░░ ░
      ░                                            ░
                       -=Bawling since 2017=-           ▒░
        ▒                                       ░
              ▒░        By: M42D                                ░
            ░          CTF: 35c3ctf
                  challege: box of blink                 ░
            ░                                         ░
                      date: 27-12-2018

              usage : cat blink.csv | ./blink.py

              notes : for best cinematic experiance adjust
                      your termial window to display a
                      resolution of 265x64 charcters

                      it's a damm shame the output wasn't
                      more animated and colorfull.

'''''''''''''''''''''''''''''''' ' ' ' '''''''''''''''''''''''''''''''''''''''''

B,A,W,L='',' ',' ',open(__file__).readlines()
for S in range(3,30):
    B+=L[S]
    if S>7 and S<13:
        A=L[S]+A
        W+=L[S]
print '\033[94m'+B+'\033[0m'
PB='\033[94m'+A+W+'\033[0m'
print "         sit back 'n enjoy"
print " "*40+"-xXx- M42D"
print PB
from time import sleep
sleep(5)
#-------------------------------------------------------------------------------
# END OF HEADER
#-------------------------------------------------------------------------------

file_out = 'catme.txt'
f = open(file_out, "w")

last_clk = '1'
last_oe  = '1'
last_lat = '1'

i=0 #string in counter
o=0 #string out counter

x=5 #knowing me x is probebly y
while 1:
    try:
        input = raw_input()
    except:
        f.close()
        print 'done..'
        print 'results saved to catme.txt'
        break
    #input skip the whole header section of the file
    i +=1
    if i > 24:
        if input == '' or input[0] == '#':
            continue

        tt = input.split(',')
        '''
        0  = TIMESTAMP
        1  = OUTPUT ENABLE    --- i guess to select matrix board 1 or 2
        2  = LATCH                               but we can ignore this
        3  = CLOCK
        4  = E    MSB --\
        5  = D           \
        6  = C            >-- ROW ADDRESS
        7  = B           /
        8  = A    LSB --/
        9  = B2  ---\
        10 = B1      \
        11 = G2       \____RGB COLORS
        12 = G1       /                B1,G1,R1 = top half of matrix
        13 = R2      /                 B2,G2,R2 = bottom half of matrix
        14 = R1  ---/
        '''
        if tt[3] != last_clk :
            last_clk = tt[3]
            last_lat = tt[2]
            last_oe = tt[1]

            adr_1 = int(''.join(tt[4:9]),2)
            adr_2 = adr_1+32

            '''
    i've used ansi-vt100 escape sequences to move cursor and change color.
    for a nice overview check: http://www.termsys.demon.co.uk/vtansi.htm


            '''
            color1 = (int(tt[10])*4)+(int(tt[12])*2)+(int(tt[14])*1)
            color2 = (int(tt[9])*4)+(int(tt[11])*2)+(int(tt[13])*1)

            line1 = "\033["+str(adr_1)+";"+str(x)+"H" #place cursor top half
            line1 +='\x1b[6;3'+str(color1)+';40m'+'█' #print a colored block
            line2 = "\033["+str(adr_2)+";"+str(x)+"H" #place cursor bottom half
            line2 +='\x1b[6;3'+str(color2)+';40m'+'█' #print a colored block
            print line1+line2
            f.write(line1+line2) # i know this slows it al down for now
                                 # but we can just cat the output later on
                                 # and hopefully see a nice animation in an
                                 # resonable frame rate.
            x +=1
        if tt[2] == "1":  #end of line
                x= 5
