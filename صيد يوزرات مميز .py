# By @SSWSG
import os,sys,subprocess,webbrowser 
subprocess.getoutput("pip install mechanize")
import requests,sys,os,time,threading

                       
import requests 
import random 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
insta="1234567890qwertyuiopasdfghjklzxcvbnm"                                                                                            # By @SSWSG
ajw="_."
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
# By @SSWSG
#logo
print ('''\033[4;31m''')
#----------------------------------------------------#
id=input(f"{F} ✓ID : {C}")
token=input(f"{F}✓ TOKEN : {C}")
# By @SSWSG
webbrowser.open('https://t.me/SSWSG ')
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
# By @SSWSG
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(W+f" » {Z} no user » {A}{user} ")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(W+f" \033[4;31m{X} BAD  : {C}{user} ")
    else:
        email=0
        print(W+f" \033[4;31m {F} GOOD : {F}{user} ")
        email+=1
        god=f"""
       ☠HIT NEW☠
────────────
√[USER ]:{user} 

√[program]: Instagram
 ────────────
TELE : @SSWSG   - @cracker_team_G """
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="1234567890..qwertyuiopasdfghjklzxvcbnm.."
    while True:
	       v = str(''.join((random.choice(insta) for i in range(1))))
	       q = str(''.join((random.choice(insta) for i in range(1))))
	       c = str(''.join((random.choice(insta) for i in range(1))))
	       kh = v+v+q+v+q
	       kh1 = v+q+'.'+v+q
	       kh2 = v+'.'+v+v+q
	       kh3 = q+'.'+v+v+v
	       kh4= v+'.'+q+'.'+q
	       kh5 = v+v+'.'+v+q
	       kh6 = q+'_'+q+'_'+v
	       kh7 = v+'_'+q+q+q
	       kh8 = q+q+q+'_'+v
	       kh9 = q+'_'+v+'_'+c
	       kh10 = q+'.'+v+'.'+c
	       kh11 = q+v+'_'+q+v
	       kh12 = '_'+v+v+q+q
	       kh13 = '_'+v+q+q+v
	       kh14 = '_'+v+q+v+v
	       kh15 = '_.'+v+q+'_'
	       kh16 = '__'+q+v+q
	       kh17 = '_'+q+'_'+v+v
	       kh18 = q+'_'+v+'.'+v
	       kh19 = q+'.'+v+'_'+v
	       kh20 = v+'__'+q+c
	       kh21 = v+q+q+'__'
	       kh22 = v+'_.'+v+q
	       khaled = kh,kh1,kh2,kh3,kh4,kh5,kh6,kh7,kh8,kh9,kh10,kh11,kh12,kh13,kh14,kh15,kh16,kh17,kh18,kh19,kh20,kh21,kh22
	       user = random.choice(khaled)
	       instaa(user)
Threads=[] 
for t in range(5):
 x = threading.Thread(target=users)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
users()

# By @SSWSG
