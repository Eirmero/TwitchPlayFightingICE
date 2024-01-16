# TwitchPlayFightingICE  
This project is built for twitch playing FightingIce game.  
Queues are used to solve the problem of message congestion, and fighting moves are preset to improve the experience.  
  
# How to start  
Please use python 3.9 or above and install the following non-standard library packages  
pip install keyboard pydirectinput pyautogui requests pynput  
  
After completing the environment setup, execute the Twitchplays program.   
  
# How to control your character  
You will play as Play2 in a fighting game in the live broadcast room. When the round starts, you will be on the right  
The commands available to you include single commands and preset combo skills  
Single command:  
right  
left  
jump  
crouch  
a1  
a2  
These commands control your character to move and attack  
Combination instructions:  
attack: initiate an attack  
persue: Pursue your enemies  
avoid: perform an urgent avoidance  
skill: Use the character’s small skills  
super: use the character’s ultimate skill when the energy is full  
  
Rememer that when your character is to the left of your opponent, you need to precede the command with   
"l:"   
This command is also because the command operated during character conversion requires orientation transformation.    
e.g. "l:attach"  
