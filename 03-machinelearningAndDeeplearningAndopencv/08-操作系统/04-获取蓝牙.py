import bluetooth

# 获取已配对的蓝牙设备信息
devices = bluetooth.discover_devices()

# 输出设备信息
for addr in devices:
    print(f"Device: {addr} ({bluetooth.lookup_name(addr)})")