
import threading
import time

import anki_vector
from anki_vector.events import Events
from anki_vector.util import degrees

got_mad = False
put_down = False
was_nice = False


def main():
    def on_state_change(robot, event_type, event, done):
        global got_mad, put_down, was_nice
        if not got_mad and robot.status.is_being_held:
            got_mad = True
            robot.behavior.set_eye_color(0.01, 1)
            robot.behavior.say_text("Don't touch me", True)
            robot.behavior.say_text("Stop. I don't want to be touched")
            robot.anim.play_animation_trigger('HeldOnPalmPickupNervous')
            robot.behavior.say_text("Put me down")
            

        if got_mad and put_down and robot.status.is_being_held and not robot.status.is_on_charger and not was_nice:
            time.sleep(2)
            robot.audio.stream_wav_file('./hi.wav', 100)
            robot.anim.play_animation_trigger('HeldOnPalmNestling')
            
            was_nice = True
            done.set()

        if got_mad and robot.status.is_on_charger and not put_down and not was_nice:
            put_down = True
            robot.behavior.set_eye_color(0.21,1)
            robot.behavior.set_lift_height(.5)
            robot.behavior.set_head_angle(degrees(0))
            time.sleep(5)
            robot.behavior.say_text('please pick me up! I want to be your friend')
            

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:


        robot.anim.load_animation_trigger_list()
        req = robot.anim.load_animation_list()
        print(req)
        done = threading.Event()
        robot.events.subscribe(on_state_change, Events.robot_state, done)
        
        if not got_mad:
            robot.behavior.say_text('do not pick me up. I do not like being touched')

        print("------ No matter what it says, pick Vector up ------")

        try:
            if not done.wait(timeout=60):
                print("------ You didn't pick up Vector! ------")
        except KeyboardInterrupt:
            pass

    robot.events.unsubscribe(on_state_change, Events.robot_state)


if __name__ == '__main__':
    main()
    