import hashlib
import requests
import random
import time

class SitePoller:
    

    def __init__(self, url, poll_interval=30):
        self.url = url
        self.poll_interval = poll_interval
    

    def get_hash(self):
        randomint = random.randint(0, 7)
        agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
        ]

        headers = {
            'User-agent': agents[randomint]
        }

        response = requests.get(self.url, headers=headers).text
        return hashlib.sha256(response.encode('utf-8')).hexdigest()
        

    def poll(self):
        current_hash = self.get_hash()

        while True:
            new_hash = self.get_hash()
            if new_hash == current_hash:
                print("No change.  Current Hash: %s" % current_hash)
            else:
                print("Changed.  Current Hash: %s" % current_hash)
            
            current_hash = new_hash
            time.sleep(self.poll_interval)
