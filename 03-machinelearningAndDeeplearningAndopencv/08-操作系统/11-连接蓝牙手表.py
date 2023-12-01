import bluetooth

nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
    print(bluetooth.lookup_name(bdaddr), bdaddr)


# import bluetooth
#
# target_name = "Your Bluetooth Headset Name"
# target_address = None
#
# nearby_devices = bluetooth.discover_devices()
#
# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name(bdaddr):
#         target_address = bdaddr
#         break
#
# if target_address is not None:
#     print("Found target bluetooth device with address ", target_address)
#     sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     sock.connect((target_address, 1))
#     print("Bluetooth connection established!")
# else:
#     print("Could not find target bluetooth device nearby")
