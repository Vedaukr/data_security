class LCGCracker():
    ADJUST = 2 << 30
    MODULUS = 2 << 31
    GEN_TYPE = "Lcg"
    a = 1664525
    c = 1013904223

    def __init__(self, client):
        self.client = client

    def crack(self):
        """
        gen_values = []
        for _ in range(3):
            is_winning, num, money = self.client.make_bet(self.GEN_TYPE, 1, 1)
            if is_winning:
                gen_values.append(1)
            else:
                gen_values.append(num)

        a, c = self.get_ac(gen_values)
        print(a, c)
        cur_value = gen_values[-1]
        while int(money) < 1000000 and is_winning:
            cur_value = (a*cur_value + c) % self.MODULUS
            is_winning, _, money = self.client.make_bet(self.GEN_TYPE, cur_value, 500)
        """
        cur_value = 1
        is_winning, num, money = self.client.make_bet(self.GEN_TYPE, cur_value, 1)
        if not is_winning:
            cur_value = int(num)

        is_winning = True
        while money < 1000000 and is_winning:
            cur_value = self.get_next(cur_value, self.a, self.c)
            is_winning, num, money = self.client.make_bet(self.GEN_TYPE, cur_value, 100)
        
        print(self.client.account_id, money)

    def get_next(self, current, a, c):
        next_value = (a*current + c) % self.MODULUS
        if next_value > self.ADJUST:
            next_value -= self.MODULUS
        return next_value

    def get_ac(self, gen_values):
        a = (gen_values[2] - gen_values[1]) * self.modinv(gen_values[1] - gen_values[0], self.MODULUS) % self.MODULUS
        c = (gen_values[1] - gen_values[0] * a) % self.MODULUS
        return a, c
    
    def euclid_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.euclid_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def modinv(self, b, n):
        g, x, _ = self.euclid_gcd(b, n)
        if g == 1:
            return x % n