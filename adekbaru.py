#coding:  utf-8

#module
import os,sys,time,getpass

os.system("clear")

x = "Adekhack"
y = "Error303"

#menulis keyboard automatic
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.020)


def login():
  sp('\033[34;1m'"     ▒██░░░▒▐█▀▀█▌░▐█▀▀▀─▐██▒██▄░▒█▌")
  sp('\033[34;1m'"     ▒██░░░▒▐█▄▒█▌░▐█░▀█▌░█▌▒▐█▒█▒█░")
  sp('\033[34;1m'"     ▒██▄▄█▒▐██▄█▌░▐██▄█▌▐██▒██░▒██▌")
  sp('\033[33;1m'"+=========================================+")
  sp('\033[31;1m'"[*]Author   : Error303"'\033[35;1m''\033[35;1m')
  sp('\033[36;1m'"[*]Whatsapp : 0168651307"'\033[35;1m')
  sp('\033[35;1m'"[*]Instagram: @era_beku")
  sp('\033[37;1m'"[*]Github   : https://github.com/amirul06")
  sp('\033[34;1m'"[*]Team     : Error Cyber Security")
  sp('\033[33;1m'"+=========================================+")
  user = raw_input('\033[34;1m'"[*]Username : "'\033[32;1m')
  pasw = raw_input('\033[34;1m'"[*]Password : "'\033[32;1m')
  if user ==x and pasw ==y:
	print '\033[32;1m'"Access Granted"
	time.sleep(2)
  else:
	print '\033[31;1m'"Access Denied"
	time.sleep(2)
	os.system("python2 loading.py")
	os.system("clear")

if __name__ == "__main__":
	login()

