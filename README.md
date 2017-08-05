# Homebrew_CPU
A record of my homebrew cpu. If you have any questions, feel free to email me at gerardkoufax@gmail.com  

I was inspired to design and build my own CPU when I saw [this video](https://www.youtube.com/watch?v=cNN_tTXABUA) and read the book it was based on, called **But how do it know?** I started by recreating the Scott CPU(described in the book) in minecraft. It worked if I recall correctly. Afterwards, I wanted to physically build it in real life, but after seeing how others had designed their own CPUs I chose to come up with my own design, thus the RSSB CPU was born(and torn to shreds a while later). The IRWIN 8 is my current design, and is partially constructed(the RAM module is complete); I'll hopefully finish it soon. The following is more detail on each CPU.

**INDEX**
* [Scott CPU](#Scott-CPU)
* [RSSB](#RSSB)
* [IRWIN 8](#Irwin-8)

# <a name="Scott-CPU"></a>Scott CPU

I don't currently have the computer or notebook that contain all the info on this CPUs construction, nor do I posses any images of what I built. I'll have them soon enough, however. So until then this section will be pretty sparse. 

# <a name="RSSB"></a>RSSB
<img src="https://github.com/Von-Braun/Homebrew_CPU/blob/master/RSSB%20notes/circuit_images/RSSB_full.PNG" height="500">  

### Why?  

I had decided on an OISC because I wanted something reasonably unique, or at least something with a quirk to it. I'd spent a long time working on the [RSSB CPU](https://en.wikipedia.org/wiki/One_instruction_set_computer#Reverse_subtract_and_skip_if_borrow) and it got quite far into the construction stage as seen in the video immediately below.  

However I made the mistake of not running it through enough tests(I only checked if output worked). That, coupled with the fact that I'm new to electronics, led to a design which never fully worked(MAR couldn't be read, making jumps difficult/impossible). As such, its parts were scrapped and used for other things.  

<a href="http://www.youtube.com/watch?feature=player_embedded&v=ZtUAzJDu5UM" target="_blank"><img src="http://img.youtube.com/vi/ZtUAzJDu5UM/0.jpg" alt="RSSB CPU" width="240" height="180" border="10" /></a>  

### Specifications: How Did The RSSB CPU Work(or not as it turned out)?
  Architecture: Harvard  
  ROM: 16-bit address(65536 cells), 8-bit data  
  RAM: 8-bit address(256 cells), 8-bit data  
  Type: [OISC(One instruction set computer)](https://en.wikipedia.org/wiki/One_instruction_set_computer)  

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

### Files  

[RSSB-NEW.py:](/RSSB%20notes/code/RSSB%20emulater%20debug) a python 2 file that emulates the RSSB CPU. You can use it if you want to write programs for the machine. Being a one instruction computer, it can be quite difficult to program.  

[un5_final.circ:](/RSSB%20notes/circuits) the circuit file made in a program called [logisim.](http://www.cburch.com/logisim/) Note that you'll need logisim to open the files.

[More notes/photos/circuits regarding the RSSB CPU](/RSSB%20notes/)  

Finally, here's a program that calulates 2+2 and outputs it( It actually calculate 2-(0-2) ):

`04 04 00 10 05 11 05 10
03 04 04 04 04 04 04 04
04 04 04 04 04 04 04 04
00 00`

I think that about sums up the RSSB CPU so we'll move on to my new design.

# <a name="Irwin-8"></a>IRWIN 8

<img src="https://github.com/Von-Braun/Homebrew_CPU/blob/master/RSSB%20notes/no_data.jpg" height="500"> 

  
