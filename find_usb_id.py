import wmi

c = wmi.WMI()
for usb in c.Win32_USBControllerDevice():
    try:
        print(usb.Dependent.DeviceID)
    except:
        continue
