from http_client import HttpClient
from lcg_cracker import LCGCracker

config = {
    "create_acc_url": "http://95.217.177.249/casino/createacc",
    "account_id": "vedaukr",
    "url": "http://95.217.177.249/casino/play{0}"
}

client = HttpClient(config)
LCGCracker(client).crack()