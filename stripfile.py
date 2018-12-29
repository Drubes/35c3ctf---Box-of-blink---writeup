#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 usage cat filename | python stripfile.py
'''

file_out = 'stripped.csv'
f = open(file_out, "w")

last_clk = '1'
last_oe  = '1'
last_lat = '1'

i=0 #string in counter
o=0 #string out counter
while 1:
    try:
        bawls=(int(last_clk)*4)+(int(last_oe)*2)+(int(last_lat)*1)
        input = raw_input('\x1b[6;3'+str(bawls)+';40m'+'█')

    except:
        print str(i)+'lines read and '+str(o)+'lines writen'
        break
    #input = raw_input(str(i)+'\n')
    i +=1
    if i > 24:
        if input == '' or input[0] == '#':
            continue
        if input == 'stop':
            break

        the_thing = input.split(',')
        '''
        0  = TIME
        1  = OUTPUT ENABLE
        2  = LATCH
        3  = CLOCK
        3  = E    MSB --\
        4  = D           \
        5  = C            >-- ROW ADDRESS 32
        6  = B           /
        7  = A    LSB --/
        8  = B2   ---\
        9  = B1       \
        10 = G2        \ pretty colors aahhwww...
        11 = G1        /
        12 = B2       /
        12 = B1  ----/
        '''
        #print the_thing
        if the_thing[3] != last_clk or the_thing[2] != last_lat or the_thing[1] != last_oe :
            f.write(input+'\n')
            last_clk = the_thing[3]
            last_lat = the_thing[2]
            last_oe = the_thing[1]
            o +=1
f.close()
