from typing import List


def brightestPosition(lights: List[List[int]]) -> int:
    events = []
    for x, y in lights:
        events.append((x - y, 1))  # Start of the light range
        events.append((x + y + 1, -1))  # End of the light range

    events.sort()
    
    max_brightness = 0
    current_brightness = 0
    brightest_position = None

    for position, event in events:
        current_brightness += event
        if current_brightness > max_brightness:
            max_brightness = current_brightness
            brightest_position = position

    return brightest_position


a = brightestPosition([[1,0],[0,1]])
print(a)
