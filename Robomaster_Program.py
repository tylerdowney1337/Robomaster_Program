### CONSTANTS ###
start = False

### MAIN MOVEMENTS ###
def start_to_one():
    # Move 7.4 m forward
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.4)
    time.sleep(2)


def one_to_two():
    # Move to corner (9.25 m)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.25)
    time.sleep(2)
    # Turn 90 degrees to the left
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    # Move to second door (7.2 m)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.2)
    time.sleep(2)


def two_to_three():
    # Move to the third door (8.85 m)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.85)
    time.sleep(2)


def three_to_four():
    # Move to the fourth door (10.2 m)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.2)
    time.sleep(2)


def four_to_three():
    # Move to the third door (10.2)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 0.2)
    time.sleep(2)


def three_to_two():
    # Move to the second door (8.85 m)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.85)
    time.sleep(2)


def two_to_one():
    # Move to the corner
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.2)
    time.sleep(2)
    # Rotate 90 degrees right
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    gimbal_ctrl.recenter()
    # Move to the first door
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.25)
    time.sleep(2)


def one_to_start():
    # Move 7.4 m to start
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.4)
    time.sleep(2)


### SCAN ROOM AND IGNORE FUNCTIONS ###
def scan_room():
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(1)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    detected_marker = vision_ctrl.get_marker_detection_info()
    print(detected_marker)
    return detected_marker[1]


def ignore_room():
    print("DANGER - ROOM TEMPERTURE EXCEEDS RECOMMENDATIONS")
    gimbal_ctrl.recenter()


def turn_180():
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()


### ROOM 1 ###
def fire_room_1():
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3)
    chassis_ctrl.move_with_distance(-90, 1.4)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    vision_ctrl.set_marker_detection_distance(1)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_five)
    detected_marker = vision_ctrl.get_marker_detection_info()
    if detected_marker[1] == 15:
        media_ctrl.play_sound(rm_define.media_custom_audio_0, wait_for_complete=False)
        time.sleep(1.25)
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        led_ctrl.gun_led_off()
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(90, 1.4)
        chassis_ctrl.move_with_distance(180, 3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)


def person_room_1():
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 1)  # 3 m
    chassis_ctrl.move_with_distance(-90, 1.25)  # 1.4 m
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    person_detected = vision_ctrl.check_condition(rm_define.cond_recognized_people)
    if person_detected:
        print("PERSON DETECTED")
        media_ctrl.play_sound(rm_define.media_custom_audio_1, wait_complete_flag=True)
        time.sleep(2)
        chassis_ctrl.move_with_distance(90, 1.25)  # 1.4 m
        chassis_ctrl.move_with_distance(180, 1)  # 3 m
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)


### ROOM 2 ###
def fire_room_2():
    pass

def person_room_2():
    pass


### ROOM 3 ###
def fire_room_3():
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(90, 1.6)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    vision_ctrl.set_marker_detection_distance(1)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_five)
    detected_marker = vision_ctrl.get_marker_detection_info()
    if detected_marker[1] == 15:
        media_ctrl.play_sound(rm_define.media_custom_audio_0, wait_for_complete=False)
        time.sleep(1.25)
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        led_ctrl.gun_led_off()
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(-90, 1.6)
        chassis_ctrl.move_with_distance(180, 4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

def person_room_3():
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(90, 1.6)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    person_detected = vision_ctrl.check_condition(rm_define.cond_recognized_people)
    if person_detected:
        media_ctrl.play_sound(rm_define.media_custom_audio_1, wait_complete_flag=True)
        time.sleep(2)
        chassis_ctrl.move_with_distance(-90, 1.6)
        chassis_ctrl.move_with_distance(-180, 4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, -90)


### ROOM 4 ###
def fire_room_4():
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, -90)
    chassis_ctrl.move_with_distance(0, 3.7)
    chassis_ctrl.move_with_distance(90, 1.55)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    vision_ctrl.set_marker_detection_distance(1)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_five)
    detected_marker = vision_ctrl.get_marker_detection_info()
    if detected_marker[1] == 15:
        media_ctrl.play_sound(rm_define.media_custom_audio_0, wait_for_complete=False)
        time.sleep(1.25)
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        led_ctrl.gun_led_off()
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(-90, 1.55)
        chassis_ctrl.move_with_distance(-180, 3.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

def person_room_4():
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.7)
    chassis_ctrl.move_with_distance(90, 1.55)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 30)
    person_detected = vision_ctrl.check_condition(rm_define.cond_recognized_people)
    if person_detected:
        print("PERSON DETECTED")
        media_ctrl.play_sound(rm_define.media_custom_audio_1, wait_complete_flag=True)
        time.sleep(2)
        chassis_ctrl.move_with_distance(-90, 1.55)
        chassis_ctrl.move_with_distance(-180, 3.7)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 270)


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set chassis translation speed to 1 m/s
    chassis_ctrl.set_trans_speed(1)
    start_to_one()
    marker = scan_room()
    # ROOM 1
    if marker == 11:
        fire_room_1()
        one_to_two()
    elif marker == 12:
        ignore_room()
        one_to_two()
    elif marker == 13:
        person_room_1()
        one_to_start()
        turn_180()
        start = True
    # ROOM 2
    if start == True:
        start_to_one()
        one_to_two()
        start = False
        marker = scan_room()
        if marker == 11:
            fire_room_2()
            two_to_three()
        elif marker == 12:
            ignore_room()
            two_to_three()
        elif marker == 13:
            person_room_2()
            two_to_one()
            one_to_start()
            turn_180()
            start = True
    else:
        marker = scan_room()
        if marker == 11:
            fire_room_2()
            two_to_three()
        elif marker == 12:
            ignore_room()
            two_to_three()
        elif marker == 13:
            person_room_2()
            two_to_one()
            one_to_start()
            turn_180()
            start = True
    # ROOM 3
    if start == True:
        start_to_one()
        one_to_two()
        two_to_three()
        start = False
        marker = scan_room()
        if marker == 11:
            fire_room_3()
            three_to_four()
        elif marker == 12:
            ignore_room()
            three_to_four()
        elif marker == 13:
            person_room_3()
            three_to_two()
            two_to_one()
            one_to_start()
            start = True
    else:
        marker = scan_room()
        if marker == 11:
            fire_room_3()
            three_to_four()
        elif marker == 12:
            ignore_room()
            three_to_four()
        elif marker == 13:
            person_room_3()
            three_to_two()
            two_to_one()
            one_to_start()
            start = True
    # ROOM 4
    if start == True:
        start_to_one()
        one_to_two()
        two_to_three()
        three_to_four()
        marker = scan_room()
        if marker == 11:
            fire_room_4()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ
        elif marker == 12:
            ignore_room()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ
        elif marker == 13:
            person_room_4()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ
    else:
        marker = scan_room()
        if marker == 11:
            fire_room_4()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ
        elif marker == 12:
            ignore_room()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ
        elif marker == 13:
            person_room_4()
            four_to_three()
            three_to_two()
            two_to_one()
            one_to_start()
            # ASQ