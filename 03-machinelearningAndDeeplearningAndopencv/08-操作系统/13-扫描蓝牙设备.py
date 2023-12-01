import bluetooth

# 扫描蓝牙设备
devices = bluetooth.discover_devices()

# 遍历设备列表，输出设备名称和 MAC 地址
for addr in devices:
    # if addr=="A8:5A:E0:4D:5D:45":
        name = bluetooth.lookup_name(addr)
        print(f'Device: {name}, MAC address: {addr}')


address = "A8:5A:E0:4D:5D:45"  # 替换为您要连接的设备的 MAC 地址
port = 1  # 默认端口为 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, port))

# 发送数据到连接的设备
sock.send("Hello, world!")

# 关闭连接
sock.close()