import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

scan_results = iface.scan_results()

import scipy.signal as signal

signal_strengths = [result.signal for result in scan_results]
frequencies = [result.frequency for result in scan_results]
# 进一步的信号分析...
