#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command Line Interface for Vector

This is an example of integrating Vector with an ipython-based command line interface.
"""

import sys
import time

try:
    from IPython.terminal.embed import InteractiveShellEmbed
except ImportError:
    sys.exit('Cannot import from ipython: Do `pip3 install ipython` to install')

import anki_vector
from anki_vector import distance_mm, speed_mms
from anki_vector.util import degrees

usage = """Use the [tab] key to auto-complete commands, and see all available methods and properties.

For example, type 'robot.' then press the [tab] key and you'll see all the robot functions.
Keep pressing tab to cycle through all of the available options.

All IPython commands work as usual.
Here's some useful syntax:
  robot?   -> Details about 'robot'.
  robot??  -> More detailed information including code for 'robot'.
These commands will work on all objects inside of the shell.

You can even call the functions that send messages to Vector, and he'll respond just like he would in a script.
Try it out! Type:
    robot.anim.play_animation_trigger('GreetAfterLongTime')
"""

args = anki_vector.util.parse_command_args()

ipyshell = InteractiveShellEmbed(banner1='\nWelcome to the Vector Interactive Shell!',
                                 exit_msg='Goodbye\n')
                                
def speak(text_to_speak):
  robot.behavior.say_text(text_to_speak)
  
def go_to_cube():
  robot.behavior.go_to_object(robot.world.connected_light_cube)
  
def pick_up_cube():
  robot.behavior.pickup_object(robot.world.connected_light_cube)
  
def put_down_cube():
  robot.behavior.place_object_on_ground_here(2) # will retry up to 2 times
  
def pop_a_wheelie_on_cube():
  robot.behavior.pop_a_wheelie(robot.world.connected_light_cube)
  
def roll_cube(): #TODO: check how much it moves doing this, could add more calls
  robot.behavior.roll_cube(robot.world.connected_light_cube)
  
# Accepts blue, orange, yellow, purple, and green will default to green if input is invalid. TODO: add more colours
def set_eye_colour(colour): 
  hue = 0.21
  saturation = 1
  if colour == 'blue':
    hue = 0.57
    saturation = 1
  elif colour == 'orange':
    hue = 0.05
    saturation = 1
  elif colour == 'yellow':
    hue = 0.11
    saturation = 1
  elif colour == 'purple':
    hue = 0.83
    saturation = 0.76
    
  robot.behavior.set_eye_color(hue, saturation)
  
def look_around():
  robot.behavior.look_around_in_place()
  
def drive_straight(mm_to_drive=100):
  if robot.status.is_on_charger:
    robot.behavior.drive_off_charger()
    
  robot.behavior.drive_straight(distance_mm(mm_to_drive))
  
def tilt_head_up():
  robot.behavior.set_head_angle(anki_vector.behavior.MAX_HEAD_ANGLE)
  
def tilt_head_down():
  robot.behavior.set_head_angle(anki_vector.behavior.MIN_HEAD_ANGLE)
  
def reset_head_to_middle():
  robot.behavior.set_head_angle(degrees(35.0))
  
# default is to only nod once. Goes back to centre position when done
def nod_head(count = 1):
  for i in range(count):
    robot.behavior.set_head_angle(anki_vector.behavior.MAX_HEAD_ANGLE)
    time.sleep(0.2)
    robot.behavior.set_head_angle(anki_vector.behavior.MIN_HEAD_ANGLE)
    time.sleep(0.2)
    robot.behavior.set_head_angle(anki_vector.behavior.MAX_HEAD_ANGLE)
  robot.behavior.set_head_angle(degrees(35))
  
# TODO: add lift behaviour
  
def turn_left():
  
def turn_right():
  
def spin around(count=1):
  

if __name__ == "__main__":
    with anki_vector.Robot(args.serial,
                           show_viewer=True) as robot:
        # Invoke the ipython shell while connected to Vector
        ipyshell(usage)
  