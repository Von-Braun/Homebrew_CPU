import msvcrt, sys,random

IAR1=0
IAR2=0
ROM=[0]*65536

MAR=0
RAM=[int(256*random.random()) for i in xrange(256)]

ACC=0
IN=0
OUT=0
'''
0=IAR
1=IAR2
2=IN
3=OUT
4=ACC
5=ZERO
6=NOP
7=NOP
8+=RAM
'''

command=raw_input('run or step: ')
if command!='step' and command!='run':
    print 'Bad argument!'
    sys.exit(0)
char = None

def keypress():
    global char
    if msvcrt.kbhit():
        char = msvcrt.getch()

def memory_map(num):
    global ACC, IN, OUT, IAR1, IAR2, RAM
    if num==0:
        return IAR1
    elif num==1:
        return IAR2
    elif num==2:
        return IN
    elif num==3:
        return OUT
    elif num==4:
        return ACC
    elif num==5:
        return 0
    elif num==6:
        return 0
    elif num==7:
        return 0
    else:
        return RAM[num]

def memory_map_asign(num):
    global ACC, IN, OUT, IAR1, RAM, IAR2
    if num==0:
        IAR1=ACC
    elif num==1:
        IAR2=ACC
    elif num==2:
        pass
    elif num==3:
        OUT=ACC
    elif num==4:
        pass
    elif num==5:
        pass
    elif num==6:
        pass
    elif num==7:
        pass
    else:
        RAM[num]=ACC
#ROM code
text=''
fr = open('input.txt', 'r')
count=0
for line in fr:
    ROM[count]=int(line)
    count+=1
"""
ROM[0]=60
ROM[1]=6
ROM[2]=6
ROM[3]=7
ROM[4]=7
ROM[5]=7
ROM[6]=6
ROM[7]=7
'''
ROM[0]=1
ROM[1]=1
ROM[2]=0
ROM[3]=5
ROM[4]=2
ROM[5]=6
ROM[6]=2
ROM[7]=5
ROM[8]=4

ROM[9]=2
ROM[10]=2
ROM[11]=2
ROM[12]=2
ROM[13]=2
ROM[14]=2
ROM[15]=2
ROM[16]=2
ROM[17]=2
ROM[18]=2
ROM[19]=2
ROM[20]=2
ROM[20]=2
ROM[21]=2
ROM[22]=2
ROM[23]=2
ROM[24]=2
ROM[25]=2
ROM[26]=2
ROM[27]=2
ROM[28]=2
ROM[29]=2
ROM[30]=2
ROM[30]=2
ROM[31]=2
ROM[32]=2
ROM[33]=2
ROM[34]=2
ROM[35]=2
ROM[36]=2
ROM[37]=2
ROM[38]=2
ROM[39]=2
ROM[40]=4
ROM[41]=4
ROM[42]=4
ROM[43]=4
ROM[44]=4
'''
"""
output_text=''
previous_out=0
#run instructions
def go():

    global IAR1,IAR2,ROM,MAR,RAM,ACC,IN,OUT,char,command,previous_out,output_text
    print '-----------------------------------------------------'
    borrow=False
    MAR=ROM[int(str(IAR2)+str(IAR1))] #set MAR
    print 'MAR: ',MAR
    if ACC>memory_map(MAR):
        borrow=True
    print memory_map(MAR),'-',ACC,'=',(memory_map(MAR)-ACC)%255
    ACC=(memory_map(MAR)-ACC)%255
    print 'ACC: ',ACC
    
    memory_map_asign(MAR)
    

    
    print 'PC :'+str(IAR1).zfill(3)+' RAM8:'+str(RAM[8]).zfill(3)
    print 'ACC:'+str(ACC).zfill(3)+' RAM9:'+str(RAM[9]).zfill(3)
    print 'IN :'+str(IN).zfill(3)+' RAM10:'+str(RAM[10]).zfill(3)
    print 'OUT:'+str(OUT).zfill(3)+' RAM11:'+str(RAM[11]).zfill(3)
    print '-----------------------------------------------------'
    if OUT!=previous_out:
        previous_out=OUT
        output_text=output_text+str(OUT)+'\n'
        fw = open('output.txt', 'w')
        fw.write(output_text)

    IAR1+=1
    if borrow: IAR1+=1

    if command=='step':
        while True:
            key=raw_input('Press enter to continue and view to see RAM: ')
            if key=='':
                break
            elif key=='view':
                print ''
                for I in range(0,len(RAM)):
                    print str(RAM[I]),
                print '\n'

if command=='run':
    for i in range(0,int(raw_input('How many steps: '))):
        go()
    raw_input('Press Enter to exit...')
elif command=='step':
    while True:
        go()


                    