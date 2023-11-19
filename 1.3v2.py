import os
while True:
	try:
	    import requests
	    import os
	    from Naked.toolshed.shell import execute_js, muterun_js
	    import sys
	    import base64
	    import threading
	    break
	except:
		os.system('pip install naked requests')
		continue
os.system('rm proxy.txt')
class mining:
    def __init__(self): 
        open('hidemycookie.txt','a')
        open('math1.js','a')
        open('math.js','a')
        self.client = requests.Session()
        self.col = {'red':'\033[91m','green':'\033[92m','yellow':'\033[93;1m','blue':'\033[94m','magenta':'\033[95m','cyan':'\033[96m','white':'\033[1;37m'}
        self.banner()
        self.hmcookie = ''
        if open('hidemycookie.txt','r').read() == '':
        	self.hmcookie = input('enter hidemy cookie[enter for skip]:'+self.col['white'])
        	open('hidemycookie.txt','a').write(self.hmcookie)
        else:
        	self.hmcookie = open('hidemycookie.txt','r').read()
        self.banner()
    def encode(self,string):
        sample_string = string
        sample_string_bytes = sample_string.encode("utf-8") 
        base64_bytes = base64.b64encode(sample_string_bytes) 
        base64_string = base64_bytes.decode("utf-8") 
        return base64_string
    def decode(self,string):
        base64_string = string
        base64_bytes = base64_string.encode("utf-8") 
        sample_string_bytes = base64.b64decode(base64_bytes) 
        sample_string = sample_string_bytes.decode("utf-8") 
        return sample_string
    def total(self):
        open('proxy.txt','a')
        data = open('proxy.txt','r').read().split('\n')
        loc = []
        for i in data:
            if i not in loc:
                loc.append(i)
        open('proxy.txt','w').write('\n'.join(loc))
        print('added '+self.col['green']+str(len(open('proxy.txt','r').read().split('\n')))+self.col['white']+' proxies')
    def banner(self):
        os.system('clear')
        orange = ["\033[38;5;202m","\033[38;5;208m","\033[38;5;214m","\033[38;5;220m","\033[38;5;226m","\033[38;5;190m"]
        #┘┌└┐
        bn = f'''
        GEN PROXXY MAX SPEED BY TMQ                                                  
        '''
        print(bn)
    def free_proxy_list(self):
        def thread1():
            data = requests.get('https://free-proxy-list.net').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        def thread2():
            data = requests.get('https://www.socks-proxy.net/').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        def thread3():
            data = requests.get('https://www.us-proxy.org/').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        def thread4():
            data = requests.get('https://free-proxy-list.net/uk-proxy.html').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        def thread5():
            data = requests.get('https://www.sslproxies.org/').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        def thread6():
            data = requests.get('https://free-proxy-list.net/anonymous-proxy.html').text
            proxy = data.split('UTC.')[1].split('<')[0].split('\n')
            proxy.pop(0)
            proxy.pop(1)
            proxy.pop(-1)
            print(f'''[{self.col['red']}+{self.col['white']}] freeproxylist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        th1 = threading.Thread(target=thread1)
        th2 = threading.Thread(target=thread2)
        th3 = threading.Thread(target=thread3)
        th4 = threading.Thread(target=thread4)
        th5 = threading.Thread(target=thread5)
        th6 = threading.Thread(target=thread6)
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th1.join()
        th2.join()
        th3.join()
        th4.join()
        th5.join()
        th6.join()
    def vpnoverview(self):
        header = {
            'method':'GET',
            'path':'/privacy/anonymous-browsing/free-proxy-servers/',
            'scheme':'https',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language':'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control':'max-age=0',
            'Cookie':'eaf_url=https//vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers/; eaf_vid=654cf08b68e267.98275717',
            'Referer':'https//duckduckgo.com/',
            'Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Linux"',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'cross-site',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

        }
        data = requests.get('https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers/',headers=header).text
        proxy = []
        cnt = data.count('<td><strong>')
        for i in range(cnt):
            proxy.append(data.split('<td><strong>')[1].split('<')[0])
            proxy[i] += ':'+data[data.index(proxy[i]):].split('</strong></td><td>')[1].split('<')[0]
            data = data.replace('<td><strong>','encrypthnglt',1).replace('</strong></td><td>','encrypthglt',1)
            print(f'''[{self.col['red']}+{self.col['white']}] vpnoverview {self.col['red']}•{self.col['white']} {i+1} proxies added {self.col['red']}•{self.col['white']} {int((i/cnt)*100)}%''',end = '\r')
        print(f'''[{self.col['red']}+{self.col['white']}] vpnoverview {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        open('proxy.txt','a').write('\n'.join(proxy))
        return open('proxy.txt','a').write('\n'.join(proxy))
    def hidemy_io(self):
        def extractdata(data,page):
            extract = []
            data = data.replace('<tr><td>','encrypthngl',1)
            while '<tr><td>' in data:
                extract.append(data.split('<tr><td>')[1].split('<')[0])
                port = data[data.index(extract[-1]):].split('</td><td>')[1].split('<')[0]
                extract[-1] += ':'+port
                data = data.replace('<tr><td>','encrypthngl',1).replace(f'</td><td>{port}<','encrypthngl',1)
            open('proxy.txt','a').write('\n'.join(extract))
            print(f'''[{self.col['red']}+{self.col['white']}] hidemy {self.col['red']}•{self.col['white']} {len(extract)} proxies added {self.col['red']}•{self.col['white']} page {page} {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            return open('proxy.txt','a').write('\n')
        try:
            header = {
                'authority':'hidemy.io',
                'method':'GET',
                'scheme':'https',
                'Cookie':self.hmcookie,
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language':'en-US,en;q=0.9,vi;q=0.8',
                'Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Sec-Fetch-Dest':'document',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-Site':'none',
                'Sec-Fetch-User':'?1',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent': (self.hmcookie.replace('%20',' ').replace('%3B',';').replace('%2F','/').replace('%2C',',').split('_uafec=')[1])[:-2]}
        except:
            header = {
                'authority':'hidemy.io',
                'method':'GET',
                'scheme':'https',
                'Cookie':self.hmcookie,
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language':'en-US,en;q=0.9,vi;q=0.8',
                'Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Linux"',
                'Sec-Fetch-Dest':'document',
                'Sec-Fetch-Mode':'navigate',
                'Sec-Fetch-Site':'none',
                'Sec-Fetch-User':'?1',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        data = self.client.get('https://hidemy.io/en/proxy-list/',headers=header).text
        extractdata(data,0)
        page = []
        for i in range(data.count('#list">')):
            page.append(data.split('#list">')[1].split('<')[0])
            data = data.replace('#list">','encrypthnglt',1)
            if page[-1] == '':
                page.pop(-1)
        page = max(list(map(int,page)))
        for i in range(1,page):
            url = f'https://hidemy.io/en/proxy-list/?start={i*64}#list'
            data = self.client.get(url,headers=header).text
            if 'Just a moment...' in data:
                print(self.col['red']+'cloudflare block'+self.col['white'])
                os.system('rm hidemycookie.txt')
                break
            extractdata(data,i)
    def proxynova(self):
        def extract(data,region):
            os.system('rm math.js')
            proxy,porta = [],[]
            cnt = data.count('<script>document.write(')
            open('math.js','a').write('function greet() {\n')
            for i in range(cnt):
                ip = data.split('<script>document.write(')[1].split(')</script>')[0]
                port = data[data.index(ip):].split('<td align="left">')[1].split('</td>')[0]
                while 'atob' in ip:
                    dec = ip.split('atob("')[1].split('"')[0]
                    ip = ip.replace(f'atob("{dec}")',f'"{self.decode(dec)}"')
                open('math.js','a').write('      console.log('+ip+');\n')
                open('math.js','a').write('      console.log(" ");\n')
                data = data.replace('<script>document.write(','encrypt',1).replace('</script>','encrypt',1)
                if 'title="Port ' in port:
                    port = port.split('title="Port ')[1].split(' ')[0]
                else:
                    port = port.replace('\n','').replace(' ','')
                if ip != '':
                    print(f'''[{self.col['red']}+{self.col['white']}] proxynova {self.col['red']}•{self.col['white']} {i} proxies added {self.col['red']}•{self.col['white']} {region} {self.col['red']}•{self.col['white']} {int((i/cnt)*100)}%''',end = '\r')
                    porta.append(port)
            open('math.js','a').write('''            }\ngreet()''')
            ip = str(muterun_js('math.js').stdout).replace('b','').replace('\\n','').replace("'",'').split(' ')
            for i in range(len(ip)-1):
                proxy.append(ip[i]+':'+porta[i])
            print(f'''[{self.col['red']}+{self.col['white']}] proxynova {self.col['red']}•{self.col['white']} {i} proxies added {self.col['red']}•{self.col['white']} {region} {self.col['red']}•{self.col['white']} 100%''',end = '\r')
            print()
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
        header = {
            'authority':'www.proxynova.com',
            'method':'GET',
            'scheme':'https',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language':'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control':'max-age=0',
            'Referer':'https//www.proxynova.com/',
            'Sec-Ch-Ua':'"Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Linux"',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

        }
        url = 'https://www.proxynova.com/'
        data = requests.get(url,headers=header).text
        for i in range(data.count('<li><a href="/proxy-server-list/country')):
            region = data.split('<li><a href="/proxy-server-list/country-')[1].split('/"')[0]
            data_prx = requests.get(f'https://www.proxynova.com/proxy-server-list/country-{region}/',headers=header).text
            extract(data_prx,region)
            data = data.replace('<li><a href="/proxy-server-list/country-','encrypt',1)
    def proxyscrape(self):
        proxy = []
        apihttp = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
        apisock4 = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all'
        apisock5 = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all'
        proxy += (requests.post(apihttp).text.replace('\r','').split('\n'))[:-1] + (requests.post(apisock4).text.replace('\r','').split('\n'))[:-1] + (requests.post(apisock5).text.replace('\r','').split('\n'))[:-1]
        open('proxy.txt','a').write('\n'.join(proxy))
        print(f'''[{self.col['red']}+{self.col['white']}] proxyscrape {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        return open('proxy.txt','a').write('\n')
    def geonode(self):
        thread = []
        def extract(url,header):
            try:
                proxy = []
                data = requests.get(url,headers=header).json()['data']
                for i in range(len(data)):
                    proxy.append(data[i]['ip']+':'+data[i]['port'])
                open('proxy.txt','a').write('\n'.join(proxy))
                print(f'''[{self.col['red']}+{self.col['white']}] geonode {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
                return open('proxy.txt','a').write('\n')
            except:
                print(self.col['red']+'get blocked from geonode'+self.col['white'],end = '\r')
                return
        header = {
            'Referer':'https//geonode.com/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        url = 'https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc'
        total = requests.get(url,headers=header).json()
        if 'message' in total:
            print(self.col['red']+'get blocked from geonode'+self.col['white'])
            return
        elif 'total' in total:
            total = total['total']
        if int(total/100) != total/100:
            total = int(total/100)+1
        else:
            total = int(total/100)
        for i in range(total):
            url = f'https://proxylist.geonode.com/api/proxy-list?limit=100&page={i+1}&sort_by=lastChecked&sort_type=desc'
            extract(url,header)
    def spys(self):
        def extract(data,region):
            try:
                jscode = data.split('</table><script type="text/javascript">')[1].split('\n')[0]
                ip = []
                for i in range(data.count('"><td colspan=1><font class=spy14>')):
                    ip.append(data.split('"><td colspan=1><font class=spy14>')[1].split('<')[0])
                    data = data.replace('"><td colspan=1><font class=spy14>','encrypt',1)
                    port = data[data.index(ip[i]):].split('document.write(')[1].split('</script>')[0]
                    jscode += f'\nconsole.log({port}'
                #print(port)
                open('math1.js','w').write(jscode.replace('</script>',''))
                port = str(muterun_js('math1.js').stdout).replace("'",'').replace('b','').replace('</font>','').replace('<font class=spy2>','').split('\\n')
                port.pop(-1)
                for i in range(len(port)):
                    ip[i] += port[i]
                print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] spys {self.col['red']}•{self.col['white']} {len(ip)} proxies added {self.col['red']}•{self.col['white']} {region} {self.col['red']}•{self.col['white']} 100%''',end = '\n')
                open('proxy.txt','a').write('\n'.join(ip))
                open('proxy.txt','a').write('\n')
            except:
                print(self.col['red']+'get banned a while from spys')
        header = {
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        def data1():
            formdata = 'xpp=5'
            url = 'https://spys.one/proxy-asn/'
            data = requests.post(url,data=formdata,headers=header).text
            for i in range(data.count("'><font class=spy6>")):
                region = data.split("'><font class=spy6>")[1].split(' <')[0]
                data = data.replace("'><font class=spy6>",'encrypt',1)
                url = ('https://spys.one/proxy-city/'+region).replace(' ','-')
                formdata ='xx0=8c2f3d8b99fa294b2084d1b087250a8c&xpp=5&xf1=0&xf2=0&xf5=0'
                datarq = requests.post(url,data=formdata,headers=header).text
                extract(datarq,region)
        def data2():
            formdata = 'xpp=5'
            url = 'https://spys.one/proxy-city/'
            data = requests.post(url,data=formdata,headers=header).text
            for i in range(data.count("'><font class=spy6>")):
                region = data.split("'><font class=spy6>")[1].split(' <')[0]
                data = data.replace("'><font class=spy6>",'encrypt',1)
                url = ('https://spys.one/proxy-city/'+region).replace(' ','-')
                formdata ='xx0=8c2f3d8b99fa294b2084d1b087250a8c&xpp=5&xf1=0&xf2=0&xf5=0'
                datarq = requests.post(url,data=formdata,headers=header).text
                extract(datarq,region)
        thread1 = threading.Thread(target=data1)
        thread2 = threading.Thread(target=data2)
        thread1.start()
        thread2.start()
    def openproxy(self):
        def thread1():
            proxy = []
            url = 'https://openproxy.space/list/http'
            data = requests.get(url).text
            for i in range(data.count(',items:[')):
                data_scrape = data.split(',items:[')[1].split(']')[0].replace('"','').split(',')
                data = data.replace(',items:[','encrypt',1)
                for i in data_scrape:
                    proxy.append(i)
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
            print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] openproxy {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        def thread2():
            proxy = []
            url = 'https://openproxy.space/list/socks4'
            data = requests.get(url).text
            for i in range(data.count(',items:[')):
                data_scrape = data.split(',items:[')[1].split(']')[0].replace('"','').split(',')
                data = data.replace(',items:[','encrypt',1)
                for i in data_scrape:
                    proxy.append(i)
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
            print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] openproxy {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        def thread3():
            proxy = []
            url = 'https://openproxy.space/list/socks5'
            data = requests.get(url).text
            for i in range(data.count(',items:[')):
                data_scrape = data.split(',items:[')[1].split(']')[0].replace('"','').split(',')
                data = data.replace(',items:[','encrypt',1)
                for i in data_scrape:
                    proxy.append(i)
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
            print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] openproxy {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        data1 = threading.Thread(target=thread1)
        data2 = threading.Thread(target=thread2)
        data3 = threading.Thread(target=thread3)
        data1.start()
        data2.start()
        data3.start()
    def proxysitelist(self):
        url = 'https://proxysitelist.net/'
        data = requests.get(url).text
        proxy = []
        for i in range(data.count('</tr><tr><td>')):
            ip = data.split('</tr><tr><td>')[1].split('<')[0]
            port = data[data.index(ip):].split('</td><td>')[1].split('<')[0]
            proxy.append(ip+':'+port)
            data = data.replace('</tr><tr><td>','encrypt',1)
        open('proxy.txt','a').write('\n'.join(proxy))
        open('proxy.txt','a').write('\n')
        print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] proxysitelist {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
    def plsource(self):
        url = 'https://proxylist.contact1777.workers.dev/'
        data = requests.get(url).text
        proxy = []
        for i in range(data.count('<tr><td>')):
            ip = data.split('<tr><td>')[1].split('<')[0]
            port = data[data.index(ip):].split('</td><td>')[1].split('<')[0]
            proxy.append(ip+':'+port)
            data = data.replace('<tr><td>','encrypt',1)
        open('proxy.txt','a').write('\n'.join(proxy))
        open('proxy.txt','a').write('\n')
        print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] plsource {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
    def rotatingproxies(self):
        url = 'https://rotatingproxies.com/free/get-proxies.php?proxy_anonymity=all&proxy_protocol=all&proxy_location=Please%20Select'
        formdata = 'proxy_anonymity=all&proxy_protocol=all&proxy_location=Please%20Select'
        header = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Referer':'https//rotatingproxies.com/free/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }
        data = requests.get(url,data=formdata,headers=header).json()
        if 'error' in data:
            print(self.col['red']+'get blocked api from rotatingproxies') 
            return
        data.pop('_links')
        data.pop('cache')
        data.pop('stats')
        proxy = []
        for i in data:
            proxy.append(data[i]['ip']+':'+str(data[i]['port']))
        open('proxy.txt','a').write('\n'.join(proxy))
        open('proxy.txt','a').write('\n')
        print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] rotatingproxies {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
    def proxylistorg(self):
        data = "Proxy('"
        proxy = []
        page = 0
        while "Proxy('" in data:
            page += 1
            url = f'https://proxy-list.org/english/search.php?p={page}'
            data = requests.get(url).text
            cnt = data.count("Proxy('")
            for i in range(cnt):
                proxy.append(self.decode(data.split("Proxy('")[1].split("'")[0]))
                data = data.replace("Proxy('",'encrypt',1)
            if cnt != 0:
                print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] proxylistorg {self.col['red']}•{self.col['white']} {i+1} proxies found {self.col['red']}•{self.col['white']} page {page} {self.col['red']}•{self.col['white']} 100%''',end = '\n')
                data = "Proxy('"
        open('proxy.txt','a').write('\n'.join(proxy))
        open('proxy.txt','a').write('\n')
        print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] proxylistorg {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
    def thespeedx(self):
        def extract(url):
            proxy = requests.get(url).text.split('\n')
            open('proxy.txt','a').write('\n'.join(proxy))
            open('proxy.txt','a').write('\n')
            print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] thespeedx {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
        th1 = threading.Thread(target=extract,args= ('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',))
        th2 = threading.Thread(target=extract,args= ('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',))
        th3 = threading.Thread(target=extract,args= ('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',))
        th1.start()
        th2.start()
        th3.start()
        th1.join()
        th2.join()
        th3.join()
    def hidemyip(self):
        url = 'https://www.hide-my-ip.com/proxylist.shtml'
        header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',}
        data = requests.get(url,headers=header).text
        json = data.split('var json = \n')[1].split(']')[0]
        proxy = []
        while '{"i":"' in data:
            proxy.append(data.split('{"i":"')[1].split('"')[0]+':'+data.split('"p":"')[1].split('"')[0])
            data = data.replace('"p":"','',1).replace('{"i":"','',1)
        open('proxy.txt','a').write('\n'.join(proxy))
        open('proxy.txt','a').write('\n')
        print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] hidemyip {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} 100%''',end = '\n')
    def freeproxyupdate(self):
        def extract(region):
            try:
                proxy = []
                url = f'https://freeproxyupdate.com/{region}'
                data = requests.get(url).text.replace('<tr>','encrypt',1)
                for i in range(data.count('<tr>')):
                    ip = data[data.index('<tr>'):].split('<td>')[1].split('<')[0]
                    port = data[data.index(ip):].split('<td>')[1].split('<')[0]
                    data = data.replace('<tr>','encrypt',1)
                    proxy.append(f'{ip}:{port}')
                open('proxy.txt','a').write('\n'.join(proxy))
                open('proxy.txt','a').write('\n')
                print(f'''{self.col['white']}[{self.col['red']}+{self.col['white']}] freeproxyupdate {self.col['red']}•{self.col['white']} {len(proxy)} proxies added {self.col['red']}•{self.col['white']} {region} {self.col['red']}•{self.col['white']} 100%''',end = '\n')
            except:
                print(self.col['red']+'get blocked from freeproxyupdate',end = '\r')
        url = 'https://freeproxyupdate.com/'
        data = requests.get(url).text
        thread = []
        for i in range(data.count('<li class="')):
            region = data[data.index('<li class="'):].split('href="/')[1].split('"')[0]
            data = data.replace('<li class="','encrypt',1)
            extract(region)
def running():
    response = mining()

    #---------------------thread
    thdg1 = threading.Thread(target=response.proxynova)
    thdg2 = threading.Thread(target=response.hidemy_io)
    thdg3 = threading.Thread(target=response.vpnoverview)
    thdg4 = threading.Thread(target=response.free_proxy_list)
    thdg5 = threading.Thread(target=response.proxyscrape)
    thdg6 = threading.Thread(target=response.geonode)
    #thdg7 = threading.Thread(target=response.spys)
    thdg8 = threading.Thread(target=response.openproxy)
    thdg9 = threading.Thread(target=response.proxysitelist)
    thdg10 = threading.Thread(target=response.plsource)
    thdg11 = threading.Thread(target=response.rotatingproxies)
    thdg12 = threading.Thread(target=response.proxylistorg)
    thdg13 = threading.Thread(target=response.thespeedx)
    thdg14 = threading.Thread(target=response.hidemyip)
    thdg15 = threading.Thread(target=response.freeproxyupdate)
    #----------------------run
    thdg1.start()
    thdg2.start()
    thdg3.start()
    thdg4.start()
    thdg5.start()
    thdg6.start()
    #thdg7.start()
    thdg8.start()
    thdg9.start()
    thdg10.start()
    thdg11.start()
    thdg12.start()
    thdg13.start()
    thdg14.start()
    thdg15.start()
    #---------------------stack
    thdg1.join()
    thdg2.join()
    thdg3.join()
    thdg4.join()
    thdg5.join()
    thdg6.join()
    #thdg7.join()
    thdg8.join()
    thdg9.join()
    thdg11.join()
    thdg12.join()
    thdg13.join()
    thdg14.join()
    thdg15.join()
    response.total()
if __name__=='__main__':   
    running()