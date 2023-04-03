# Vector

This is a repo for all work in progress files for the Vector anthropomorphism module.

## Files
* `pickup.py` will make Vector react first negatively to being picked up and then positively. It could be used as an example in part 1 of the module. the file `hi.wav` is required for execution.

* `cliff.py` will first make Vector drive toward the edge of a table (it should be positioned close to the edge) and then stop. Then, it will make Vector backup and do the same thing without stopping. If the user doesn't intervene Vector will fall. This was initially written for another module idea but could be adapted into an example for part 1 of the module. **This will be updated to a scenario where Vector runs into his cube which students will imagine is very dangerous for him. For example, the cube could be a bomb**

* `interactive_shell.py` is based example provided by Anki. It opens up an iPython environment and streams what Vector sees to the laptop. It now contains simplified wrappers over Vector functionality that students can call in the iPython environment.

* `danger.py` is an extension of `cliff.py`. In this program, the vector will first go towards the cliff, come back and then say that "I am going to crash into a very dangerous object, I might die!" and once the user picks him up and will change his path from crashing the vector will then say "Thanks for saving my life".
<br>
<br>

## Running example module 1
#### MacOS 
1. Open the terminal app (or your preferred emulator)
2. Navigate to where `pickup.py` is located. *If you do not know how to navigate via the command line the easiest thing is to put the file in your "Documents" file and then run `cd documents` after opening the terminal app*
3. Type `python3 pickup.py` into your terminal and press enter
4. The program should now be running

### Windows
*TODO: test this with a windows machine just to make sure*
1. Open Command Prompt (or your preferred emulator)
2. Navigate to where `pickup.py` is located. *If you do not know how to navigate via the command line the easiest thing is to put the file in your "Documents" file and then run `cd documents` after opening Command Prompt*
3. Type `python3 pickup.py` into your terminal and press enter
4. The program should now be running

#### Interacting with the program
* Vector will start by speaking, no matter what it says you should then pick it up off its charger
* Once it has stopped moving/speaking, place it back on its charger
* Wait for Vector to speak again and then pick it up for the second time

<br>
<br>

## Using the interactive environment

### Pre-requisites
* The SDK is installed on your machine *(documentation on this step to be completed)*
* You've connected a Vector to your laptop
* Your Python version is no higher than 3.7.7
* iPython is installed. If it is not you may install it by running `python3 -m pip install ipython` *TODO: Check this on Windows*
* You've downloaded `interactive_shell.py` and know where it is in your file directory

### Starting the environment
#### MacOS 
1. Open the terminal app (or your preferred emulator)
2. Navigate to where `interactive_shell.py` is located. *If you do not know how to navigate via the command line the easiest thing is to put the file in your "Documents" file and then run `cd documents` after opening the terminal app*
3. Type `Python3 interactive_shell.py` into your terminal and press enter
4. You should now see the iPython environment in your terminal!

### Windows
*TODO: test this with a windows machine just to make sure*
1. Open Command Prompt (or your preferred emulator)
2. Navigate to where `interactive_shell.py` is located. *If you do not know how to navigate via the command line the easiest thing is to put the file in your "Documents" file and then run `cd documents` after opening Command Prompt*
3. Type `Python3 interactive_shell.py` into your terminal and press enter
4. You should now see the iPython environment in your terminal!

### Running commands
You may run Python commands one line at a time. Below is a list of pre-defined, simplified functions you can call and what each will do. To run a command type the function (ex. `look_around()` into your terminal and press enter. Vector should then perform the specified action(s).

#### Running multiple commands at once
If you'd like to write more advanced Python code or queue up multiple commands before running them, you may create a new lines in the interactive shell without running the first line you've written. Once you've written one line and don't press enter; instead use the keyboard shortcut below to create a new line and then navigate down to it. You may repeat this to create as many lines as you would like. 
* On MacOS: <kbd>⌃ Control</kbd> + <kbd>O</kbd>
* On Windows: <kbd>CTRL</kbd> + <kbd>O</kbd>


*TODO: these commands should ideally be hosted elsewhere where we can have them automatically update based on in-line documentation. They should also be sorted by category/functionality.*
| Function    | Description | Example |
| ----------- | ----------- | ------- |
| `speak(text)`  | Vector will say the text that you write in the brackets | `speak('hello human')` |
| `go_to_cube()` | Vector will go to its light cube if it is reachable |
| `pick_up_cube()` | Vector will go to its cube if it is reachable and pick it up |
| `put_down_cube()` | Vector will put down its cube. If it cannot put it down it will retry twice |
| `pop_a_wheelie()` | Vector will use its cube to pop a wheelie. The cube must be available |
| `roll_cube()` | (*tentative*) Vector will roll its cube |
| `set_eye_colour(colour)` | Vector's eye colour will change to the specified colour. Accepts blue, orange, yellow, purple, and green will default to green if input is invalid. | `set_eye_colour(blue)` |
| `look_around()` | Vector will look around without moving |
| `drive_straight(distance)` | Vector will drive straight forward. Distance must be in millimetres. If no distance is specified it will drive 100mm.| `drive_straight(20)` |
| `tilt_head_up()` | Vector will tilt its head up as far as it can go |
| `tilt_head_down()` | Vector will tilt its head down as far as it can go |
| `move_head_to_middle()` | Vector's head will move to the middle position. It will be facing forward |
| `nod_head(repetitions)` | Vector will nod its head a specified number of times. If nothing is specified Vector will nod once | `nod_head(3)` |

