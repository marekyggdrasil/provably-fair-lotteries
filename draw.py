import sys

from src.lottery import lottery

rn = int(sys.argv[1])
key = sys.argv[2]

input_hash = sys.argv[3]
seed, tickets, shuffled = lottery(input_hash, rn)

print('{0:13}: {1:34}'.format('lottery name', key))
print('{0:13}: {1:34}'.format('tickets count', str(rn)))
print('{0:13}: {1:34}'.format('seed hash', input_hash))
print('{0:13}: {1:34}'.format('seed int', str(seed)))
print()
print('Tickets')
print(tickets)
print()
print('Shuffled')
print(shuffled)
