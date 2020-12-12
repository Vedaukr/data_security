from mt19937 import MT19937
from datetime import datetime, timedelta
from abstract_cracker import AbstractCraker

class MtCracker(AbstractCraker):
    GEN_TYPE = "Mt"

    def crack(self):
        start_num = 1
        is_winning, num, account = self.client.make_bet(self.GEN_TYPE, start_num, 1)
        if not is_winning:
            start_num = num

        creation_date = datetime.strptime(account['deletionTime'].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        start_time = int((creation_date).timestamp())
        end_time = int((creation_date + timedelta(hours=2)).timestamp())
        self.gen = self._search(start_time, end_time, 1, start_num)
        self.win_casino(1)

    def get_next(self, current):
        return self.gen.get_random_number()

    def _search(self, start_time, end_time, delta, start_num):
        for seed in range(start_time, end_time, delta):
            g = MT19937(seed)
            if g.get_random_number() == start_num:
                print(seed)
                return g