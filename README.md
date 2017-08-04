# Homebrew_CPU
A record of my homebrew cpu. If you have any questions, feel free to email me at gerardkoufax@gmail.com

**INDEX**
* [RSSB](#RSSB)
* [IRWIN 8](#Irwin-8)

## <a name="RSSB"></a>RSSB
<img src="https://github.com/Von-Braun/Homebrew_CPU/blob/master/RSSB%20notes/circuit_images/RSSB_full.PNG" height="500">  

[Notes/photos/circuits regarding the RSSB CPU](/RSSB%20notes/)

I was inspired to design and build my own CPU when I saw [this video](https://www.youtube.com/watch?v=cNN_tTXABUA) and read the book it was based on, called **But how do it know?** I spent a long time working on an [RSSB CPU](https://en.wikipedia.org/wiki/One_instruction_set_computer#Reverse_subtract_and_skip_if_borrow) and it got quite far into the construction stage as seen in the video below.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=ZtUAzJDu5UM
" target="_blank"><img src="http://img.youtube.com/vi/ZtUAzJDu5UM/0.jpg" 
alt="RSSB CPU" width="240" height="180" border="10" /></a>

However I made the mistake of not running it through enough tests(I only checked if output worked). That, coupled with the fact that I'm new to electronics, led to a design which never fully worked(MAR couldn't be read, making jumps difficult/impossible). As such, its parts were scrapped and used for other things.

* ### How Did The RSSB CPU Work(or not as it turned out)?

* The CPU loops through the following sequence infinitely:
  1. A = register or RAM_address    #that's the english word or, not a logical or.
  2. Acc = A - Acc
  3. A = Acc
  4. IAR = IAR + 1
  5. If step 2 resulted in a negative number do: IAR = IAR + 1
  
* The memory was mapped in the following way(the numbers are addresses):  
  0 = IAR  
  1 = IAR2  
  2 = In  
  3 = Out  
  4 = Acc  
  5 = Zero  
  6 = NOP?
  7 = NOP?
  Anything above 7 is treated as an address in RAM
  
The circuit below is what's responible for the two parts above(i.e. the memory-mapping and 5-step-loop):  

<img src="https://github.com/Von-Braun/Homebrew_CPU/blob/master/RSSB%20notes/circuit_images/RSSB_CU.PNG" height="500">  

[Here](/RSSB%20notes/code/RSSB%20emulater%20debug) you'll find a python 2 file that emulates the RSSB CPU. You can use it if you want to write programs for the machine. Being a one instruction computer, it can be quite difficult to program. [These](/RSSB%20notes/circuits) are the circuit files made in a program called [logisim.](http://www.cburch.com/logisim/) Note that you'll need logisim to open the files.

Finally, here's a program that calulates 2+2 and outputs it( It actually calculate 2-(0-2) ):

`04 04 00 10 05 11 05 10
03 04 04 04 04 04 04 04
04 04 04 04 04 04 04 04
00 00`

I think that about sums up the RSSB CPU so we'll move on to my new design.

## <a name="Irwin-8"></a>IRWIN 8

<img src="https://github.com/Von-Braun/Homebrew_CPU/blob/master/RSSB%20notes/no_data.jpg" height="500"> 

  
