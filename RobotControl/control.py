from ClientClass import client
from pynput import keyboard

user = client()

while True:
    msg = input("Message : ")
    user.send(msg)

    if msg == "Man":
        print("Manual mode")


        def on_press(key):

            if key == keyboard.Key.esc:
                return False
            else:
                while True:
                    try:
                        keyc = key.char
                        break
                    except:
                        pass

                if keyc == 'w':
                    user.send("W")
                if keyc == 'a':
                    user.send("A")
                if keyc == 's':
                    user.send("S")
                if keyc == 'd':
                    user.send("D")
                if keyc == 'c':
                    user.send("Color")
                if keyc == 'x':
                    user.send("Distance")


        def on_release(key):
            user.send("stop")


        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

        user.send("end")

    elif msg == "Follow":
        print("Now robot will be following the black line")
