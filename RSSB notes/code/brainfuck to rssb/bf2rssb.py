text=''
fr = open('input.txt', 'r')
for line in fr:
    text=text+line
print text
output_text=''#'10\n10\n9\n9\n0\n9\n0\n4\n4\n0\n10\n0\n4\n9\n10\n0\n9\n10\n10\n'

max_length=9 #the longest instruction
MAR=6
RAM_START=8
count=0
count_resets=0
#pad count and erase IAR after. count is counting all rather than resetting at 256 to 0
for i in text:
    #old_length=(len(output_text)/2)-(256*count_resets)
    if count>=256-(max_length*2): #increase IAR2 automatically
        #print 'over',
        pad='0\n'*(257-(count+5)) #257 is because the 0 address is never run, 9 is the length of th IAR2+=1 command
        print 'over', count,(257-(count+5))
        output_text=output_text+'4\n7\n5\n0\n'+'1'+'\n'+pad+'4\n4\n' #IAR2 is incremented first immediatly moving the code to IAR2[01] IAR[EF]. jumps to IAR2[01] IAR[01] if IAR2[01] IAR[EF] == 00, 00
        count=2
        #old_length=0

    if i=='+':
        output_text=output_text+'4\n7\n5\n0\n'+str(RAM_START)+'\n4\n4\n'
        count+=7
    elif i=='-':
        output_text=output_text+'4\n7\n'+str(RAM_START)+'\n4\n4\n'
        count+=5
    elif i=='.':
        output_text=output_text+'4\n3\n3\n'+str(RAM_START)+'\n5\n4\n3\n4\n4\n'
        count+=9
    elif i=='>':
        #output_text=output_text+'4\n7\n5\n0\n'+str(MAR)+'\n4\n4\n'
        RAM_START+=1
    elif i=='<':
        #output_text=output_text+'4\n7\n'+str(MAR)+'\n4\n4\n'
        RAM_START-=1
    #count=(len(output_text)/2)-(256*count_resets)
    print count, i

output_text=output_text+'4\n7\n5\n0\n'+'1'+'\n'#end program
fw = open('output.txt', 'w')
fw.write(output_text)