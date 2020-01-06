import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP_s VP

    NP_s -> NP_common | Pron_n 
    N_new -> N | N N_new 
    
    NP_o -> NP_common |  Pron_o
    
    NP_common -> Name | Det N_new | Det AdjP N_new| Det N_new PP | Det AdjP N_new PP | AdjP Name
    
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
    Aux_Vi_be_pre -> AdvP Aux_be_past | Aux_be_past
    
    VP_Aux -> Aux_Vi_pp Vi_pp | Aux_Vi_pp AdvP Vi_pp | Aux_Vi_pp Vi_pp AdvP
    Aux_Vi_pp -> Aux_have | Aux_model Aux_have_pres
    Aux_have -> Aux_have_pres | Aux_have_past
    
    VP_Aux -> Aux_Vt_pp Vt_mono_pp | Aux_Vt_pp AdvP Vt_mono_pp | Aux_Vt_pp Vt_mono_pp AdvP
    Aux_Vt_pp -> Aux_be_passive |  Aux_model Aux_be_pres | Aux_have_be_pre | Aux_have_be_pre Aux_be_prog
    
    VP_Aux -> Aux_model Vi | Aux_model AdvP Vi | Aux_model Vi AdvP
    
    
    
    Name -> 'Nadia' | 'Ross' | 'Marseilles' | 'Google'
    N -> 'fur' | 'cat' | 'eggplant' | 'rutabaga' | 'boat' | 'poodle' | 'autoclave' | 'cloth' | 'cheese' | 'man' | 'elephant' | 'hovercraft' | 'autopoiesis' | 'help' | 'menu' | 'shoot' | 'demand' | 'reward'
    
    Vi -> 'demand' | 'give' | 'win' | 'believe' | 'jump' | 'shoot' | 'aspire' | 'help' | 'boat' | 'leave' | 'eat' | 'arrive' | 'see'			
    Vi_sp -> 'demanded' | 'gave' | 'won' | 'believed' | 'jumped' | 'shot' | 'aspired' | 'helped'| 'boated' |'left' | 'ate' | 'arrived' | 'saw'				
    Vi_pp -> 'demanded' | 'gave' | 'won' | 'believed' | 'jumped' | 'shot' | 'aspired' | 'helped' | 'boated' | 'left' | 'eaten' | 'arrived' | 'seen'					
    Vi_pg -> 'demanding' | 'giving' | 'winning' | 'believing' | 'jumping' | 'shooting' | 'aspiring' | 'helping' | 'boating' | 'leaving' | 'eating' | 'arriving' | 'seeing'
        
    Vt_mono -> 'reward' | 'demand' | 'find' | 'give' | 'remind' | 'want' | 'win' | 'believe' | 'jump' | 'tell' | 'bring' | 'fondle' | 'shoot' | 'leave' | 'have' | 'help' | 'eat' | 'boat' | 'see'
    Vt_mono_sp -> 'rewarded' | 'demanded' | 'found' | 'gave' | 'reminded' | 'wanted' | 'won' | 'believed' | 'jumped' | 'told' | 'brought' | 'fondled' | 'shot' | 'left' | 'had' | 'helped' | 'ate' | 'boated' | 'saw'
    Vt_mono_pp -> 'rewarded' | 'demanded' | 'found' | 'given' | 'reminded' | 'wanted' | 'won' | 'believed' | 'jumped' | 'told' | 'brought' | 'fondled' | 'shot' | 'left' | 'helped' | 'eaten' | 'boated' | 'seen'
    
    Vt_di -> 'demand' | 'give' | 'remind' | 'tell' | 'bring'
    Vt_di_sp -> 'demanded' | 'gave' | 'reminded' | 'told' | 'brought'
    Vt_di_pp -> 'demanded' | 'given' | 'reminded' | 'told' | 'brought'
    
    Aux_model -> 'can' | 'may' | 'could' | 'should' | 'might' | 'must' | 'would' | 'will'
    
    Aux_have_pres -> 'have' | 'has'
    Aux_have_past -> 'had'
    Aux_have -> 'have'
    
    Aux_be_passive -> 'are' | 'were' | 'is' | 'was' | 'am'
    Aux_be_past -> 'been'
    Aux_be_pres -> 'be'
    Aux_be_prog -> 'being'
    
    P -> 'with' | 'in' | 'on' | 'by' | 'after' | 'before' | 'from' | 'of' | 'to' | 'onto' | 'for'
    Adv -> 'immediately' | 'slowly' | 'already' | 'always' | 'really'
    Adj -> 'long' | 'soft' | 'tall' | 'handsome'
    Det -> 'the' | 'a' | 'an' | 'her' | 'my'  
    
    Pron_n -> 'I' | 'he' | 'she' | 'it' | 'we' | 'they' | 'you'
    Pron_p -> 'my' | 'your' | 'his' | 'her' | 'their'
    Pron_o -> 'me' | 'him' | 'her' | 'us' | 'them'                                      
""")

print("==========================")

a2_test = """the cat with the long soft fur ate slowly with Nadia
the cat with the long soft fur slowly ate with Nadia
Nadia slowly ate
Nadia ate slowly
she ate slowly
the cat with the long soft fur was eating
the cat with the long soft fur was slowly eating with Nadia
Nadia was eating slowly with her long fur cat
Nadia was eating slowly with her long fur cat
she was slowly eating with her cat
Nadia had left with her cat
the cat with the long soft fur had eaten
the cat with the long soft fur had slowly eaten with Nadia
Nadia had eaten slowly with her long fur cat
Nadia had eaten slowly with her long fur cat
she had slowly eaten with her cat
Nadia had been slowly eating with her long fur cat
Nadia had been eating slowly with her long fur cat
Nadia had already been eating with her long fur cat
her cat with the long soft fur had been eating slowly with Nadia
her cat with the long soft fur had been slowly eating
she had been slowly eating with her long fur cat
Nadia leave immediately
Nadia immediately leave
Nadia leave immediately
Nadia arrived with her long cat
she leave immediately
Nadia is slowly eating with her long fur cat
Nadia is slowly eating with her long fur cat
Nadia is eating slowly with her long fur cat
her cat with the long soft fur is eating slowly with Nadia
her cat with the long soft fur is slowly eating with Nadia
she is slowly eating with her long fur cat
Nadia has left
she has left
Nadia has left immediately
Nadia has immediately left
Nadia has immediately left with her long soft eggplant
Nadia has left immediately with her long soft eggplant
Nadia have been slowly eating with her long fur cat
Nadia have been eating slowly with her long fur cat
Nadia have already been eating with her long fur cat
her cat with the long soft fur have been eating slowly with Nadia
her cat with the long soft fur have been slowly eating
she have been slowly eating with her long fur cat
Nadia has left immediately
Nadia has immediately left
Nadia has immediately left with her long soft eggplant
Nadia has left immediately with her long soft eggplant
Nadia have been slowly eating with her long fur cat
Nadia have been eating slowly with her long fur cat
Nadia have already been eating with her long fur cat
her cat with the long soft fur have been eating slowly with Nadia
her cat with the long soft fur have been slowly eating
she have been slowly eating with her long fur cat
Nadia will leave
Nadia will leave immediately
Nadia will immediately leave
Nadia will leave slowly with her cat
her cat with the long soft fur will leave slowly with Nadia
she will leave
Nadia will be leaving 
Nadia will be leaving immediately
Nadia will be immediately leaving 
Nadia will be leaving slowly with her cat
her cat with the long soft fur will be leaving slowly with Nadia
she will be leaving 
Nadia will have left
she will have left
Nadia will have left immediately
Nadia will have immediately left
Nadia will have immediately left with her long soft eggplant
Nadia will have left immediately with her long soft eggplant
Nadia will have been eating
she will have been eating
the long soft cat will have been eating with Nadia
the long soft eggplant is eaten by handsome Nadia
she is seen slowly by her cat 
she is slowly seen by her cat 
the long soft eggplant was eaten by handsome Nadia
she was seen slowly by her cat 
she was slowly seen by her cat 
Nadia was slowly eaten by the long soft eggplant
she will be seen slowly by her cat
she have been slowly eaten by the long soft eggplant 
she have been eaten slowly by the long soft eggplant
she had been slowly eaten by the long soft eggplant 
she had been eaten slowly by the long soft eggplant
the long eggplant will be eaten by the long cat
the long eggplant have been being eaten by Nadia"""


parser = nltk.ChartParser(grammar)
a2_test_list = [s.split() for s in a2_test.split('\n')]
print("A2 Zhao TEST=====")
count = 0
for s in a2_test_list:
    try:
        #print("==========================")
        if not len(list(parser.parse(s))) > 0:
            count += 1
            words = ' '.join(s)
            print(words)
        # print(len(list(parser.parse(s))) > 0)
    except Exception as e:
        print(e)
print(count)