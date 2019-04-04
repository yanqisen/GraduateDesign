import sys
sys.path.append('/Users/yanqisen/GraduateDesign/GraduateDesign')
from utils import  URLDECODE

a="/yk10/?page=54%20LIMIT%201%2C1%20UNION%20ALL%20SELECT%20NULL%2C%20NULL%2C%20NULL%23"
print(URLDECODE(a))
f=open("")
for line in open('test_normal.txt','r'):
    if len(line):
        urldecode=urllib.parse.unquote(line)
