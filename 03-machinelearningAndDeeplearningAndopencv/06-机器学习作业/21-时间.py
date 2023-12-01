import  time

timestamp=1734567895
localtime=time.localtime(timestamp)
print(localtime)
formattime=time.strftime("%Y-%m-%d",localtime)
print(formattime)