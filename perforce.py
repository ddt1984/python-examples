# Peforce에서 파일 다운로드
from P4 import P4,P4Exception

p4 = P4()
p4.port = "PERFORCE_HOST:PORT"
p4.user = "USERNAME"
p4.password = "PASSWORD" # MD5
p4.client = "P4_CLIENT"

try:
    p4.connect()
except P4Exception as err:
    print(err)

path = "//PERFORCE_PATH/TeamName.xlsx"
p4.run("print", "-o", "samples/TeamName.xlsx", path)
