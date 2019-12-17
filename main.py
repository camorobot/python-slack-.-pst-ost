########################
# TO DO
########################
# 1 find ost and pst files on the computer
# 2 import slack api
# 3 make a .zip file off all pst and ost files
# 4 upload .zip file with the slack api
########################
# INFO
########################
# command promt: dir /s *.pst /AND/ dir /s *.ost
########################

import os
import subprocess
from slacker import Slacker

TOKEN = open('TOKEN.txt', 'r')
TOKENKEY = TOKEN.readline()

slack = Slacker(TOKENKEY)

message = "test"
slack.chat.post_message('#random',message);
