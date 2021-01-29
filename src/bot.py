import time
import pyautogui
import yaml
import os
import time


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('Took time: %2.2f sec Elements: %r Speed: %2.1f sec/tel' % (te - ts, len(args[0]),(te - ts)/len(args[0])))
        return result

    return timed


# Init
with open('config/param.yml') as stream:
    config = yaml.safe_load(stream)

# Init variable
IMAGE_FOLDER = config['IMAGE_FOLDER']
TIMEOUT_IN_SEC = config['TIMEOUT_IN_SEC']
MAX_COUNT_TO_EXIT = config['MAX_COUNT_TO_EXIT']
EXCEPTION_MSG_CANNOT_CLICK = config['EXCEPTION_MSG_CANNOT_CLICK']
EXCEPTION_MSG_CANNOT_DELETE_FILES = config['EXCEPTION_MSG_CANNOT_CLICK']
INPUT_LIST_NUMBER = config['INPUT_LIST_NUMBER']


def delete_content_from_dir(dir_path):
    try:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                os.remove(os.path.join(root, file))
        return True
    except:
        return False


def click_by_image(image_name, lang, os, confidence=.9, grayscale=True):
    i = 1
    while True:
        file_name = f'{os}_{lang}_{image_name}.png'
        path = f'{IMAGE_FOLDER}/{file_name}'
        location = pyautogui.locateOnScreen(path, grayscale=grayscale, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        else:
            time.sleep(TIMEOUT_IN_SEC)
            if i == MAX_COUNT_TO_EXIT:
                # print(f"cannot find image {file_name}")
                return False
            i += 1


@timeit
def viber_user_checker(list_number):


    pyautogui.hotkey('Win')
    pyautogui.typewrite('Viber')
    pyautogui.keyDown('Enter')


    click_by_image("btn_not_full_screen", "en", "win")

    if not click_by_image("btn_call", "en", "win"):
        raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

    if not click_by_image("btn_show_dialer", "en", "win"):
        raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

    # Cleanup avatar photo
    if not delete_content_from_dir('static/images/avatars/'):
        raise Exception(EXCEPTION_MSG_CANNOT_DELETE_FILES)

    for telephone_number in list_number:

        # focus on enter number
        if not click_by_image("btn_phone_dialer", "en", "win"):
            click_by_image("btn_send_message", "en", "win")

        pyautogui.typewrite(telephone_number)

        # touch user via mesage
        if not click_by_image("btn_send_message", "en", "win"):
            if not click_by_image("btn_call", "en", "win"):
                raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

            if not click_by_image("btn_show_dialer", "en", "win"):
                raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

            pyautogui.typewrite(telephone_number)
            click_by_image("btn_send_message", "en", "win")

        # get details of the user
        click_by_image("btn_show_user_details", "en", "win")

        # # close user details
        # if not click_by_image("btn_hide_user_details", "en", "win"):
        #     raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

        # check if user have viber
        if click_by_image("btn_user_does_not_have_viber", "en", "win"):
            print(f"{telephone_number} is not viber")
        else:
            x, y, h, w = pyautogui.locateOnScreen(f"{IMAGE_FOLDER}/win_en_btn_marker_for_screenshot.png")

            #time.sleep(1)
            if click_by_image("btn_user_offline", "en", "win"):

                print(f"{telephone_number} is offline")
            else:
                if click_by_image("btn_user_online", "en", "win"):
                    print(f"{telephone_number} is online")
                else:
                    print(f"{telephone_number} is hidden")
            screenshot = pyautogui.screenshot(region=(x + 50, y - 250, 300, 300))
            screenshot.save(f"static/images/avatars/{str(telephone_number).replace('+', '')}.png")

    # exit from viber
    if not click_by_image("btn_viber_exit", "en", "win"):
        raise Exception(EXCEPTION_MSG_CANNOT_CLICK)

    return True


if __name__ == '__main__':
    # clean and compact list
    list_number = INPUT_LIST_NUMBER.split(" ")
    list_number = list(map(str.strip, list_number))  # trim all element
    list_number = list(filter(bool, list_number))  # trim empty element
    # main runtime
    viber_user_checker(list_number)
