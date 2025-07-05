import wmi
import time
import winsound
import pymsgbox

LOG_FILE = "logs.txt"
AUTHORIZED_FILE = "authorized_devices.txt"

def log_event(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {msg}\n")
    print(msg)

def load_authorized_devices():
    try:
        with open(AUTHORIZED_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def get_connected_usb_ids():
    c = wmi.WMI()
    usb_ids = []
    for usb in c.Win32_USBControllerDevice():
        try:
            device_id = usb.Dependent.DeviceID
            if device_id.startswith("USB\\VID_"):  # Only allow real USB devices (not ROOT_HUB or Bluetooth)
                usb_ids.append(device_id)
        except:
            continue
    return usb_ids

def play_alert():
    # Simple beep sound: frequency 1000Hz, duration 1000ms (1 second)
    winsound.Beep(1000, 1000)

def show_popup(msg):
    pymsgbox.alert(msg, "USB Alert")

def monitor_usb():
    log_event("USB monitoring started.")
    authorized_ids = load_authorized_devices()
    previously_seen = set()

    while True:
        current_usb = set(get_connected_usb_ids())

        new_devices = current_usb - previously_seen
        for device in new_devices:
            log_event(f"USB Inserted: {device}")
            if device not in authorized_ids:
                log_event(f"⚠️ Unauthorized USB detected: {device}")
                play_alert()
                show_popup("⚠️ Unauthorized USB Detected!")

        removed_devices = previously_seen - current_usb
        for device in removed_devices:
            log_event(f"USB Removed: {device}")

        previously_seen = current_usb
        time.sleep(5)

if __name__ == "__main__":
    monitor_usb()
