import winsound

#define  a     3830    // 261 Hz 
#define  b     3400    // 294 Hz 
#define  c     3038    // 329 Hz 
#define  d     2864    // 349 Hz 
#define  e     2550    // 392 Hz 
#define  f     2272    // 440 Hz 
#define  g     2028    // 493 Hz 
#define  A     1912    // 523 Hz 
#// Define a special note, 'R', to represent a rest
#define  R     0
a=261
b=294
c=329
d=349
e=392
f=440
g=493
A=523
R=0
melody = [e,b,c,d,c,b,a,a,c,e,d,c,b,c,d,e,c,a,a  ,d,f,A,g,f,e,c,e,d,c,b,b,c,d,e,c,a,a]
beats = [2, 1, 1,  2,  1,  1, 2, 1, 1, 2, 1, 1, 3,  1,  2,  2, 2, 2, 4  ,2,1,2,1,1,3,1,2,1,1,2,1,1,2,2,2,2,2] 
for i in range(len(melody)):
    print i
    winsound.Beep(melody[i], beats[i]*160)