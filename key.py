from Crypto.PublicKey import RSA
import random


class Message:
    e = 65537
    N = ""
    _d = ""
    x0 = 0
    x1 = 0

    def generate_RSA(self):
        bits = 2048
        new_key = RSA.generate(bits, e=65537)
        public_key = new_key.publickey().exportKey("PEM")
        private_key = new_key.exportKey("PEM")
        return private_key, public_key

    def generate_value(self):
        return random.randint(0, 100)

    def send_Key(self):
        m1=Message()
        m1.N,m1.d= generate_RSA()
        m1.x0=generate_value()
        m1.x1=generate_value()
        self.send(m1.N)
