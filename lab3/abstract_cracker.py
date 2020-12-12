class AbstractCraker():
    GEN_TYPE = ""
    def __init__(self, client):
        self.client = client

    def win_casino(self, value):
        while True:
            value = self.get_next(value)
            is_winning, _, account = self.client.make_bet(self.GEN_TYPE, value, 100)
            if not is_winning or account['money'] > 1000000:
                break
        
        print(self.client.account_id, account['money'])
    
    def get_next(self, cur_value):
        pass