from src.lottery import lottery


def test_grin_block_hash():
    rn = 12
    input_hash = '00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893'
    seed, tickets, shuffled = lottery(input_hash, rn)
    assert seed == 434826832662083618074763177596269117349512691366460603804297690115782803
    assert tickets == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert shuffled == [12, 5, 8, 9, 6, 11, 1, 4, 3, 7, 2, 10]
