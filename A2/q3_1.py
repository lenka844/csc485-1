import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
        
    NP -> Name | Det N_new | Det AdjP N_new| Det N_new PP | Det AdjP N_new PP | Pron_n 
    N_new -> N | N N_new 
    
    VP -> V
    VP -> VP AdvP | AdvP VP 
    VP -> VP PP
    
    AdvP -> Adv | AdvP Adv
    AdjP -> Adj | Adj AdjP
    PP -> P NP
    
    
    Name -> 'Nadia'
    N -> 'fur' | 'cat'
    V -> 'left' | 'arrived' | 'ate'
    
    P -> 'with' | 'in' | 'on'
    Adv -> 'immediately' | 'slowly'
    Adj -> 'long' | 'soft' | 'tall' | 'handsome'
    Det -> 'the' | 'her'
    
    Pron_n -> 'I' | 'he' | 'she' | 'it' | 'we' | 'they' | 'you'
    Pron_p -> 'my' | 'your' | 'his' | 'her' | 'their'
    Pron_o -> 'me' | 'him' | 'her' | 'us' | 'them'                                     
""")

sent = ["Nadia left immediately",
        "the cat with the long soft fur slowly ate",
        "Nadia ate slowly",
        "her cat with the long soft fur slowly ate"]

wrong_sent = ["Nadia with the long soft fur slowly ate",
              "the cat with the tall her arrived"]

parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent[1].split()):
    #print(tree)
    tree.draw()
