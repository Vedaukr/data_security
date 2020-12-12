from mt19937 import MT19937
from datetime import datetime, timedelta
from abstract_cracker import AbstractCraker
import ctypes

# Inspired By https://jazzy.id.au/2010/09/22/cracking_random_number_generators_part_3.html
class ImprovedMtCracker(AbstractCraker):
    GEN_TYPE = "BetterMt"
    ITER_COUNT = 624

    def crack(self):
        inputs = []
        for _ in range(self.ITER_COUNT):
            guess_num = 1
            is_winning, num, account = self.client.make_bet(self.GEN_TYPE, guess_num, 1)
            if not is_winning:
                guess_num = num
            inputs.append(guess_num)

        
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

    def _un_bitshift_right_xor(self, value -> ctypes.c_int, shift -> ctypes.c_int) -> ctypes.c_int:
        i = ctypes.c_int(0)
        result = ctypes.c_int(0)
        while (i * shift < 32) {
            partMask = (ctypes.c_int(-1) << (ctypes.c_int(32) - shift)) >>> (shift * i);
            // obtain the part
            int part = value & partMask;
            // unapply the xor from the next part of the integer
            value ^= part >>> shift;
            // add the part to the result
            result |= part;
            i++;
        }