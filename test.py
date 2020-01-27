from time import time
from datetime import datetime

f = open('log/log.txt', 'a+', encoding="utf-8")
for i in range(10):
    f.writelines('Hello world!\t' + str(datetime.fromtimestamp(time())) + str(i) + '\n')
f.close()
