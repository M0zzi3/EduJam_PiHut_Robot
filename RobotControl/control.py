from ClientClass import client
from pynput import keyboard

user = client()


def manual_mode():
    print("Manual mode")

    def on_press(key):

        if key == keyboard.Key.esc:
            print('')
            user.send("end")
            return False
        else:
            while True:
                try:
                    keyc = key.char
                    break
                except:
                    pass

            if keyc == 'w':
                user.send("forward")
            if keyc == 'a':
                user.send("left")
            if keyc == 's':
                user.send("backward")
            if keyc == 'd':
                user.send("right")
            if keyc == 'c':
                user.send("color")
            if keyc == 'x':
                user.send("distance")
            if keyc == 'r':
                user.send('gear_up')
            if keyc == 'f':
                user.send('gear_down')

    def on_release(key):
        user.send("stop")

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


user_commands = {
    "Man": manual_mode
}

while True:
    msg = input("Message : ")
    user.send(msg)

    try:
        user_commands.get(msg)()

    except:
        pass
