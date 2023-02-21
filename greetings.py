import sys
from datetime import datetime

jenkins_param = str(sys.argv[1])
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
gret_msg = f'Hello {jenkins_param}, good luck!'

print(gret_msg)
print("Current Time =", current_time)

