from src.lottery import lottery


# grin lottery #1
# block height 1550360
# https://grinexplorer.net/block/00003fdaff2ab03fcbdeed39307a4ad90c0bbf4394d23026b7b4b794d8f6b932
def test_grinventions_1():
    rn = 25
    input_hash = '00003fdaff2ab03fcbdeed39307a4ad90c0bbf4394d23026b7b4b794d8f6b932'
    seed, tickets, shuffled = lottery(input_hash, rn)
    assert seed == 440714160416639244135458261333621959951537644246447821549491272723904818
    assert tickets == list(range(1, rn+1))
    assert shuffled == [10, 16, 24, 12, 5, 18, 25, 20, 19, 22, 6, 9, 14, 23, 21, 15, 13, 8, 3, 7, 4, 1, 17, 2, 11]


# anteaters lottery #1
# block height 1545578
# https://grinexplorer.net/block/00006f2e7a304290afb47c35064fb0f7462f127a26d51f47ff1a22b1076ba5fd
def test_anteaters_1():
    rn = 22
    input_hash = '00006f2e7a304290afb47c35064fb0f7462f127a26d51f47ff1a22b1076ba5fd'
    seed, tickets, shuffled = lottery(input_hash, rn)
    assert seed == 767346869993045883512611938304905359464618715524261301224426443209680381
    assert tickets == list(range(1, rn+1))
    assert shuffled == [10, 14, 4, 2, 6, 12, 7, 11, 1, 9, 8, 19, 16, 17, 18, 5, 15, 21, 22, 20, 3, 13]


# just a test
def test_grin_block_hash():
    rn = 12
    input_hash = '00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893'
    seed, tickets, shuffled = lottery(input_hash, rn)
    assert seed == 434826832662083618074763177596269117349512691366460603804297690115782803
    assert tickets == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert shuffled == [12, 5, 8, 9, 6, 11, 1, 4, 3, 7, 2, 10]
