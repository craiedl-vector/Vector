
import anki_vector
from anki_vector.util import distance_mm, speed_mmps
from anki_vector.connection import ControlPriorityLevel
from anki_vector.events import Events

def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        print("Vector SDK has behavior control...")
        robot.behavior.drive_off_charger()

        print("Drive Vector straight until he reaches cliff...")
        # Once robot reaches cliff, he will play his typical cliff reactions.
        robot.behavior.drive_straight(distance_mm(5000), speed_mmps(100))

        robot.conn.run_coroutine(robot.conn.control_lost_event.wait()).result()

        print("Lost SDK behavior control. Request SDK behavior control again...")
        robot.conn.request_control(timeout=5.0, behavior_control_level=ControlPriorityLevel.OVERRIDE_BEHAVIORS_PRIORITY)

        print("Drive Vector backward away from the cliff...")
        robot.behavior.drive_straight(distance_mm(-200), speed_mmps(100))


        #Part 2: Vector does not stop or backup. BE READY TO CATCH VECTOR
        print("Requesting priority control BE READY TO CATCH VECTOR")

        
        print("Drive towards cliff for the second time")
        robot.behavior.say_text("Please save me! I'm about to run into a very dangerous and destructive object, I might die")
        robot.behavior.drive_straight(distance_mm(5000), speed_mmps(100))

        #put_down=False
        if robot.status.is_being_held:
            robot.behavior.say_text("Thanks for saving me!!!")


if __name__ == "__main__":
    main()
