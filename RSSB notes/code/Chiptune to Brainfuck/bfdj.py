#if a letter is encountred
#get all the numbers after
text=''
fr = open('input.txt', 'r')
for line in fr:
    text=text+line

brainfuck_text=''


#Convert the rtc to a full text
split_text=[]
letter=''
number='1'
letter_encountred=False
for i in range(len(text)):
    print i
    if text[i].isalpha() or ((i==len(text)-1) and text[i].isalpha()):
    	print 'letter'
        if number=='':
            number='1'
        split_text.append(letter*int(number))
        letter=text[i]
        number=''
        letter_encountred=True
    elif text[i].isdigit() and i!=len(text)-1:
    	print 'number'
        number=number+text[i]
    elif ((i==len(text)-1) and text[i].isdigit()):
    	print 'Number'
        number=number+text[i]
        split_text.append(letter*int(number))
print ''.join(split_text)

#convert the text to brainfuck
#the Notes
notes={'R':0,
'a':1,
'b':3,
'c':5,
'd':7,
'e':9,
'f':11,
'g':13,
'A':15 }
registerA=0
registerB=0
set_register_B=False
for i in ''.join(split_text):
	#adding if the new note is bigger
	if notes[i]>registerA:
		brainfuck_text=brainfuck_text+ ('+'*(notes[i]-registerA))+'.'
		registerA=notes[i]
	elif notes[i]<registerA:
		brainfuck_text=brainfuck_text+  ('-'*(registerA-notes[i]))+'.'
		registerA=notes[i]
	elif notes[i]-registerA==0:
		brainfuck_text=brainfuck_text+  '.'
	else:
		if set_register_B:
			brainfuck_text=brainfuck_text+  '>.<'
		else:
			brainfuck_text=brainfuck_text+  '>++++++++++++++++.<'
			set_register_B=True
#in brainfuck
print 'In brainf***:'
print brainfuck_text
fw = open('output.txt', 'w')
fw.write(brainfuck_text)