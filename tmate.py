import os
import sys
email = sys.argv[1]
tmate = sys.argv[2]

os.system('sudo apt update')

os.system('sudo apt install nano')
os.system('sudo apt-get install tmate -y')

os.system('tmate -k tmk-{} -n {}'.format(email,tmate)
