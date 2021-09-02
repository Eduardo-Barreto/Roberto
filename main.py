from roberto_control import move_circle
from os import system

move_circle('down')
system('git add .')
system('git commit -m "update table"')
system('git push')
