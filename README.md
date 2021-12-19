# provably-fair-lotteries

## How to run the lottery?

To run lottery named `grinventions-giveaway-1` for `12` tickets distributed and seed hash `00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893` from [block 1,532,392](https://grinexplorer.net/block/00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893) do

```sh
python draw.py 12 grinventions-giveaway-1 00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893
```

and that will give you

```
lottery name : grinventions-giveaway-1           
tickets count: 12                                
seed hash    : 00003f009fa5b002fb32efde6f7924409a3a745f79fcfcfa2e5221489710b893
seed int     : 434826832662083618074763177596269117349512691366460603804297690115782803

Tickets
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Shuffled
[12, 5, 8, 9, 6, 11, 1, 4, 3, 7, 2, 10]
```

### Compatibility

Lottery result will be the same if run under the following Python versions
```
3.4, 3.5, 3.6, 3.7, 3.8, 3.9
```

## Current lotteries

TODO

## Past lotteries

TODO

