from speedtest import  Speedtest
net=Speedtest()
download=net.download()
upload=net.upload()
print(f"您当前的网速为{upload/1024/1024}Mbps")