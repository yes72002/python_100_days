import pyautogui, cv2
import keyboard

# Set a pause between each action
pyautogui.PAUSE = 0.1

# Set detect point
detect_point = [430, 738] # chrome dinasaur

def mouse_pixel():
    # Get current mouse position
    mouse = pyautogui.position()
    mouse_x = mouse[0]
    mouse_y = mouse[1]
    print(f"mouse position = {mouse}")
    mouse_pixel = pyautogui.pixel(mouse_x, mouse_y)
    print(f"mouse pixel = {mouse_pixel}")

def chrome_dinosaur():
    coord = pyautogui.pixel(detect_point[0], detect_point[1])
    if coord[0] == 83 and coord[1] == 83:
        pyautogui.press('space')


if __name__ == "__main__":
    while True:
        # Activate bot when ESC key is pressed
        if keyboard.is_pressed('esc'):
            # mouse_pixel() # for pre setting
            chrome_dinosaur()
