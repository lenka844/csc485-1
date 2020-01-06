import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP_s VP

    NP_s -> NP_common | Pron_n 
    N_new -> N | N N_new 
    
    NP_o -> NP_common | Pron_o
    
    NP_common -> Name | Det N_new | Det AdjP N_new| Det N_new PP | Det AdjP N_new PP | AdjP Name | N_new
    
    AdvP -> Adv | AdvP Adv
    AdjP -> Adj | Adj AdjP
    
    VP -> VP_simple | VP_complex
    VP_simple -> Vi_sp | Vi
    VP_simple -> VP_simple AdvP | AdvP VP_simple
    VP_simple -> VP_simple PP
    
    PP -> P NP_o | P Pron_o
    VP_complex -> VP_Aux
    VP_complex -> VP_Aux AdvP | VP_Aux
    VP_complex -> VP_Aux PP
    
    VP_Aux -> Aux_Vi_pg Vi_pg | Aux_Vi_pg AdvP Vi_pg | Aux_Vi_pg Vi_pg AdvP
    Aux_Vi_pg -> Aux_be_passive | Aux_have_be_pre | Aux_model Aux_be_pres | Aux_model Aux_have Aux_Vi_be_pre
    
    Aux_have_be_pre -> Aux_have_pres Aux_Vi_be_pre | Aux_have_past Aux_Vi_be_pre
    Aux_Vi_be_pre -> AdvP Aux_be_past | Aux_be_past AdvP | Aux_be_past
    
    VP_Aux -> Aux_Vi_pp Vi_pp | Aux_Vi_pp AdvP Vi_pp | Aux_Vi_pp Vi_pp AdvP
    Aux_Vi_pp -> Aux_have | Aux_model Aux_have_pres
    Aux_have -> Aux_have_pres | Aux_have_past
    
    VP_Aux -> Aux_Vt_pp Vt_mono_pp | Aux_Vt_pp AdvP Vt_mono_pp | Aux_Vt_pp Vt_mono_pp AdvP
    Aux_Vt_pp -> Aux_be_passive |  Aux_model Aux_be_pres | Aux_have_be_pre | Aux_have_be_pre Aux_be_prog
    
    VP_Aux -> Aux_model Vi | Aux_model AdvP Vi | Aux_model Vi AdvP
    
    VP_simple -> VP_mono_normal NP_o | V_mono_normal NP_o PP
    V_mono_normal -> Vt_mono_sp | AdvP Vt_mono_sp | Vt_mono_sp AdvP
    
    VP_simple -> V_mono_normal NP_o V_to Vi PP | VP_simple V_to Vi
    
    VP_simple -> Vt_di_normal NP_o NP_o| Vt_di_normal NP_o NP_o PP
    Vt_di_normal -> Vt_di_sp | advP Vt_di_sp | Vt_di_sp advP
    
    VP_simple -> V_mono_normal conj NP_s VP_simple
    VP_simple -> Aux_be_passive NP_o | Aux_be_passive PP | Aux_be_passive AdvP PP


    
    
    Name -> 'Nadia'
    N -> 'fur' | 'cat' | 'eggplant'
    
    Vi -> 'leave' | 'eat' | 'eat' | 'arrive' | 'see' | 'jump'			
    Vi_sp -> 'left' | 'ate' | 'arrived' | 'saw' | 'jumped'			
    Vi_pp -> 'left' | 'eaten' | 'arrived' | 'seen' | 'jumped'					
    Vi_pg -> 'leaving' | 'eating' | 'arriving' | 'seeing' | 'jumping'			
    
    Vt_pp -> 'eaten' | 'seen' | 'jumped'
    
    Aux_model -> 'can' | 'may' | 'could' | 'should' | 'might' | 'must' | 'would' | 'will'
    
    Aux_have_pres -> 'have' | 'has'
    Aux_have_past -> 'had'
    Aux_have -> 'have'
    
    Aux_be_passive -> 'are' | 'were' | 'is' | 'was' | 'am'
    Aux_be_past -> 'been'
    Aux_be_pres -> 'be'
    Aux_be_prog -> 'being'
    
    P -> 'with' | 'in' | 'on' | 'by'
    Adv -> 'immediately' | 'slowly' | 'already' | 'extremely'
    Adj -> 'long' | 'soft' | 'tall' | 'handsome'
    Det -> 'the' | 'her'
    
    Pron_n -> 'I' | 'he' | 'she' | 'it' | 'we' | 'they' | 'you'
    Pron_p -> 'my' | 'your' | 'his' | 'her' | 'their'
    Pron_o -> 'me' | 'him' | 'her' | 'us' | 'them'                                         
""")

a2_test = """Nadia with the long soft fur slowly ate
her arrived with her cat
the the cat arrived
she reminded the handsome man to eat the elephant
the the cat arrived long
the cat with the tall her arrived
the cat with the tall her arrived with she
her cat with the tall she arrived
she cat with the tall she arrived
the cat the cat arrived
the cat long arrived
the cat arrived arrived
the cat with the long soft fur the cat with the long soft fur slowly ate
Nadia ate slowly ate slowly slowly
Nadia ate with her handsome extremely cat
Nadia ate handsome slowly
Nadia will left
Nadia has could leave
Nadia has had left
her cat may is seen with Nadia
her cat is arrived 
Nadia have been see with her cat
Nadia have be seen with her cat
Nadia may has been seen with her cat
her cat is is seen
Nadia eaten
Nadia is eat 
Nadia had have left
Nadia had been see with her cat
Nadia had be seen with her cat
Nadia had had arrived 
Nadia have been could seen with her cat
Nadia immediately has been seen with her cat
Nadia have leave
Nadia with the long soft fur ate slowly with Nadia
Nadia with the long soft fur eaten slowly with Nadia
Nadia with the long soft fur eating slowly with Nadia
she had ate with her cat
her cat with long fur eating with Nadia
Nadia may had been seen
Nadia may is eaten
Nadia may be is eating
Nadia may is being eating
Nadia already had been eating with her long fur cat
the long eggplant have been being eat by Nadia
the long eggplant have been being being eaten by Nadia
the long eggplant have had been eating
the long eggplant already have been eating
she will have leave
she will jumped
she will have been jump
she is have being seen
Nadia with long fur had being been seen
Nadia has will immediately left"""

parser = nltk.ChartParser(grammar)
a2_test_list = [s.split() for s in a2_test.split('\n')]
print("A2 Zhao TEST=====")
count = 0
for s in a2_test_list:
    try:
        #print("==========================")
        if len(list(parser.parse(s))) > 0:
            count += 1
            words = ' '.join(s)
            print(words)
        # print(len(list(parser.parse(s))) > 0)
    except Exception as e:
        print(e)
print(count)

wrong_sent = ["Nadia immediately has been seen with her cat"]
for tree in parser.parse(wrong_sent[0].split()):
    #print(tree)
    tree.draw()