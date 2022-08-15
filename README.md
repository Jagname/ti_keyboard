# ⌨ ti_keyboard

## ti_keyboard is a small library allowing to interact with the keyboard of your TI calculator (developed for TI-83 Premium CE Python edition with french keys)

> The provided library has been compacted to use as little space as possible on the calculator, that's why you will find all the docstrings below.

> The modes represent whether the key was pressed in normal, second or alpha mode. You can find a list of all the keys at the bottom.

* ### get_key(k):
        Allows you to obtain the name of a key by specifying its associated number.

* ### key_pressed():
        Call this function to find out which key the user has pressed.
        
        >>> key = key_pressed()
        >>> if key == 'LEFT':
        >>>     player.backward(...)
        >>> elif key == 'RIGHT':
        >>>     player.forward(...)

* ### is_pressed(k, duration=float('inf'), mode=normal):
        Give a key (it's possible to specify the mode: second or alpha).
        If the key is pressed, returns True.
        Else, returns False.

        Specify the argument duration if you want to give a time limit (in seconds) to press the key.

        Don't call this function in a loop, use key_pressed() with conditions instead.

        >>> if is_pressed('entrer'):
        >>>     restart()
        >>> else:
        >>>     exit()

* ### combo():
        Give a list of keys, if these keys are pressed successively, returns True.
        Else, returns False.

        Specify the argument duration if you want to give a time limit (in seconds) to make the combo.
        Specify the argument kp if you want to embed a combo in a loop:
        
        >>> while True:
        >>>     kp = key_pressed()
        >>>     if kp == 'LEFT':
        >>>         print("to the left")
        >>>     elif kp == 'RIGHT':
        >>>         print("to the right")
        
        >>>     if combo([1, 4, 7], duration=3, kp=kp):
        >>>         print("Successful combo!")

# Normal Mode 

'f(x)' : 73,  
'fenetre' : 72,  
'zoom' : 46,  
'trace' : 90,  
'graphe' : 68,  
'mode' : 69,  
'suppr' : 10,  
'UP' : 3,  
'RIGHT' : 1,  
'DOWN' : 4,  
'LEFT' : 2,  
'X,T,theta,n' : 180,  
'stats' : 49,  
'math' : 50,  
'matrice' : 55,  
'prgm' : 45,  
'var' : 53,  
'annul' : 9,  
'<>' : 64018,  
'trig' : 64017,  
'resol' : 64020,  
':/:' : 64458,  
'^' : 132,  
'x²' : 189,  
',' : 139,  
'(' : 133,  
')' : 134,  
'/' : 131,  
'log' : 193,  
'7' : 149,  
'8' : 150,  
'9' : 151,  
'*' : 130,  
'ln' : 191,  
'4' : 146,  
'5' : 147,  
'6' : 148,  
'-' : 129,  
'sto' : 138,  
'1' : 143,  
'2' : 144,  
'3' : 145,  
'+' : 128,  
'on' : 0,  
'0' : 142,  
'.' : 141,  
'(-)' : 140,  
'entrer' : 5  

# Second Mode

'f(x)' : 48,  
'fenetre' : 75,  
'zoom' : 87,  
'trace' : 59,  
'graphe' : 74,  
'mode' : 64,  
'suppr' : 11,  
'RIGHT' : 15,  
'LEFT' : 14,  
'X,T,theta,n' : 65,  
'stats' : 58,  
'math' : 51,  
'matrice' : 182,  
'prgm' : 47,  
'var' : 56,  
'<>' : 57,  
'trig' : 181,  
'resol' : 44,  
':/:' : 64016,  
'x²' : 190,  
',' : 152,  
'(' : 236,  
')' : 237,  
'/' : 239,  
'log' : 194,  
'7' : 249,  
'8' : 250,  
'9' : 251,  
'*' : 135,  
'ln' : 192,  
'4' : 246,  
'5' : 247,  
'6' : 248,  
'-' : 136,  
'sto' : 12,  
'1' : 243,  
'2' : 244,  
'3' : 245,  
'+' : 54,  
'0' : 62,  
'.' : 238,  
'(-)' : 197,  
'entrer' : 13  

# Alpha Mode

'math' : 154,  
'matrice' : 155,  
'prgm' : 156,  
'<>' : 157,  
'trig' : 158,  
'resol' : 159,  
':/:' : 160,  
'^' : 161,  
'x²' : 162,  
',' : 163,  
'(' : 164,  
')' : 165,  
'/' : 166,  
'log' : 167,  
'7' : 168,  
'8' : 169,  
'9' : 170,  
'*' : 171,  
'ln' : 172,  
'4' : 173,  
'5' : 174,  
'6' : 175,  
'-' : 176,  
'sto' : 177,  
'1' : 178,  
'2' : 179,  
'3' : 204,  
'+' : 203,  
'0' : 153,  
'.' : 198,  
'(-)' : 202

