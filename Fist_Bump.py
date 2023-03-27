import anki_vector
from anki_vector.util import degrees

def fist_bump(robot):
    robot.anim.play_animation_trigger('GreetAfterLongTime')
    robot.behavior.drive_off_charger()
    robot.behavior.set_lift_height(1.0)
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.drive_straight(distance_mm(50), speed_mmps(100))
    robot.behavior.set_lift_height(0.0)
    robot.anim.play_animation_trigger('FistBumpSuccess')
    robot.behavior.drive_straight(distance_mm(-50), speed_mmps(100))
    robot.behavior.set_head_angle(degrees(0.0))

def main():
    with anki_vector.Robot() as robot:
        robot.conn.request_control()
        voice_recognition = robot.behavior.say_text("Hey Vector! Can you give me a fist bump?")

        # Check if the voice command is recognized
        if voice_recognition:
            # Perform the fist bump
            fist_bump(robot)

            # Respond with "Sure thing, bud!"
            robot.behavior.say_text("Sure thing, bud!")

main()
