import requests 
import random
import datetime
#r = requests.get(url = URL, params = PARAMS) 

GEN_TYPES = ['Lcg', 'Mt']

class HttpClient():

    def __init__(self, config):
        self.url = config['url']
        
        acc_created = False
        while not acc_created:
            acc_num = random.randint(1, 20202020)
            account_id = config['account_id'] + str(acc_num)
            params = {'id': account_id}
            result = requests.get(url=config['create_acc_url'], params=params).json()
            acc_created = not 'error' in result
        
        self.account_id = account_id
        #self.account_id = config['account_id']

    def make_bet(self, gen_type, number, bet):
        if not gen_type in GEN_TYPES:
            return
        
        params = {
            'id': self.account_id,
            'bet': bet,
            'number': number
        }

        url = self.url.format(gen_type)
        result = requests.get(url=url, params=params).json()
        return self._is_win_message(result['message']), result['realNumber'], result['account']

    def _is_win_message(self, message):
        return message != "You lost this time"