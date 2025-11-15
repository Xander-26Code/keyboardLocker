from pynput import keyboard
is_locked = False
def on_hotkey_activate():
    global is_locked
    is_locked = not is_locked
    print("--- KEYBOARD {} ---".format("LOCKED" if is_locked else "UNLOCKED"))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse("<command>+<shift>+L"),
    on_hotkey_activate
)
def for_canonical(f):
    return lambda k: f(listener.canonical(k))