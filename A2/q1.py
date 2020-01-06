import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    S -> VP
    S -> Aux NP VP
    S -> NP-where Aux NP VP
    S -> NP-wh VP
    S -> NP-wh Aux NP VP-wh
    NP -> N
    NP -> Det N
    NP -> Adj N
    PP -> P NP
    VP -> V Adv | V
    VP -> V NP Adv
    VP -> V NP Adv PP
    VP-wh -> V Adv | V Adv PP | V PP | V
    Det -> 'the' | 'their' | 'your'
    Adj -> 'old' | 'red' | 'happy'
    Adv -> 'quickly' | 'slowly'
    N -> 'dogs' | 'parks' | 'statues' | 'people'
    V -> 'race' | 'walk' | 'eat'
    P -> 'in' | 'to' | 'on' | 'under' | 'with'
    Aux -> 'should' | 'will'
    NP-wh -> 'who' | 'what'
    NP-where -> 'where'
""")

sent = ["who walk their dogs quickly in parks",
        "what will people walk quickly in parks",
        "where should people walk their dogs quickly",
        "should people walk their dogs quickly in parks"]

wrong_sent = ["what people walk quickly in parks",
              "what should people walk their dogs quickly in parks",
              "where walk their dogs quickly in parks"]

parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent[1].split()):
    print(tree)

