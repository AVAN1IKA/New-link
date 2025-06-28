#THE LAST FILE WAS DELETED BECAUSE IT HAS DONE A BREAKAGE TO MY THINKING CAPACITY OF SOLVING ERROR

#DIGI_CLOCK

import time
while True:
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)

#OUTPUT: if you not stop it , this will continue showing you output one after another 
#TERMINAL: if you not stop the terminal the output will continue running like a digital watch 
#the differnece is we see new output with past output in OUTPUT DISPLAY whereas in TERMINAL we see the time actually changing like a digital watch , where the seconds are changing 