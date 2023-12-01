import asyncio
from bleak import BleakClient
from Crypto.Cipher import AES
import time

AuthKey = "手环Auth Key"
Truekey = bytes.fromhex(AuthKey)
Mac = "手环Mac地址"
CHARACTERISTIC_AUTH = "00000009-0000-3512-2118-0009af100700"
CHARACTERISTIC_HEART_RATE_CONTROL = "00002a39-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_HEART_RATE_MEASURE = "00002a37-0000-1000-8000-00805f9b34fb"
_send_enc_key = b'\x03\x00'
global cmd


def notification_handler(sender, data):
    if len(data) == 2:
        a = data.hex()[2:4]
        b = int(a, 16)
        print(b)
    elif data[:3] == b'\x10\x02\x01':
        random_nr = data[3:]
        global Truekey
        aes = AES.new(Truekey, AES.MODE_ECB)
        truedata = aes.encrypt(random_nr)
        global cmd
        cmd = _send_enc_key + truedata
        print("创建密钥完成")


async def main(address):
    global cmd
    client = BleakClient(address)
    print("连接中")
    client._timeout = 100
    await client.connect()
    await client.start_notify(CHARACTERISTIC_AUTH, notification_handler)
    print("验证中")
    await client.write_gatt_char(CHARACTERISTIC_AUTH, b'\x02\x00')
    await asyncio.sleep(1.0)
    await client.write_gatt_char(CHARACTERISTIC_AUTH, cmd)
    await asyncio.sleep(1.0)
    await client.start_notify(CHARACTERISTIC_HEART_RATE_MEASURE, notification_handler)
    print("连接完成，请稍等十秒左右完成首次测量")
    await client.write_gatt_char(CHARACTERISTIC_HEART_RATE_CONTROL, b'\x15\x02\x00', True)
    await asyncio.sleep(1.0)
    await client.write_gatt_char(CHARACTERISTIC_HEART_RATE_CONTROL, b'\x15\x01\x00', True)
    await asyncio.sleep(1.0)
    await client.write_gatt_char(CHARACTERISTIC_HEART_RATE_CONTROL, b'\x15\x01\x01', True)
    t = time.time()
    while True:
        time.sleep(1)
        if (time.time() - t) >= 12:
            await client.write_gatt_char(CHARACTERISTIC_HEART_RATE_CONTROL, b'\x16', True)
            t = time.time()


asyncio.run(main(Mac))