import random

def lottery(seed_hex, rn):
    seed = int.from_bytes(bytes.fromhex(seed_hex.replace('0x', '')), 'big')
    tickets = list(range(1, rn+1))
    shuffled = list(tickets)
    random.Random(seed).shuffle(shuffled)
    return seed, tickets, shuffled
