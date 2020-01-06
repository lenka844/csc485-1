import nltk

grammar = nltk.CFG.fromstring("""
    
    S -> NP_s VP

    NP_s -> NP_common | Pron_n 
    
    NP_o -> NP_common | Pron_o
    
    NP_common -> NPrp | AdjP NPrp | N_new | AdjP N_new | N_new PP | N_new PP | AdjP N_new PP
NP_common -> Det N_new | Det AdjP N_new | Det N_new PP | Det AdjP N_new PP
N_new -> N | N N_new
    
    AdvP -> Adv | AdvP Adv
    
    AdjP -> Adj | Adj AdjP

    VP -> VP_simple | VP_complex
    
    VP_simple -> Vi_sp
VP_simple -> VP_simple AdvP | AdvP VP_simple
VP_simple -> VP_simple PP

    VP_complex -> VP_Aux
    VP_complex -> VP_Aux AdvP
    VP_complex -> VP_Aux PP | VP_Aux PP AdvP
    
    PP -> P NP_o | P Pron_o | PP PP 

    VP_Aux -> Aux_Vi_pg Vi_pg | Aux_Vi_pg AdvP Vi_pg | Aux_Vi_pg Vi_pg AdvP
Aux_Vi_pg -> Aux_be_passive | Aux_have_be_pre | Aux_modal_Adv Aux_be_pres | Aux_modal_Adv Aux_have Aux_Vi_be_pre
Aux_modal_Adv -> Aux_modal | Aux_modal AdvP
    
    Aux_have_be_pre -> Aux_have_pres Aux_Vi_be_pre | Aux_have_past Aux_Vi_be_pre
Aux_Vi_be_pre -> AdvP Aux_be_past | Aux_be_past AdvP | Aux_be_past
    

   VP_Aux -> Aux_Vi_pp Vi_pp | Aux_Vi_pp AdvP Vi_pp | Aux_Vi_pp Vi_pp AdvP
Aux_Vi_pp -> Aux_have_pres | Aux_have_past | Aux_modal_Adv Aux_have
    

    VP_Aux -> Aux_Vt_pp Vt_mono_pp | Aux_Vt_pp AdvP Vt_mono_pp | Aux_Vt_pp Vt_mono_pp AdvP
Aux_Vt_pp -> Aux_be_passive | Aux_modal_Adv Aux_be_pres | Aux_have_be_pre | Aux_have_be_pre Aux_be_prog_Adv | Aux_modal_Adv Aux_have Aux_Vt_be_Adv
Aux_Vt_pp -> Aux_be_passive Aux_be_prog_Adv | Aux_modal_Adv Aux_be_pres Aux_be_prog_Adv | Aux_be_passive Aux_be_prog_Adv
    Aux_Vt_be_Adv -> AdvP Aux_be_past_pg | Aux_be_past_pg AdvP | Aux_be_past_pg
Aux_be_past_pg -> Aux_be_past | Aux_be_past Aux_be_prog_Adv
Aux_be_prog_Adv -> AdvP Aux_be_prog | Aux_be_prog

   VP_Aux -> Aux_modal_Adv Vi | Aux_modal_Adv AdvP Vi | Aux_modal_Adv Vi AdvP
    
    VP_simple -> V_mono_Adv NP_o
    V_mono_Adv -> Vt_mono_sp | AdvP Vt_mono_sp | Vt_mono_sp AdvP
    
   PP -> V_to Vi | V_to Vt_mono NP_o | V_to Vt_di NP_o NP_o
 
    VP_simple -> Vt_di_Adv NP_o NP_o
    Vt_di_Adv -> Vt_di_sp | advP Vt_di_sp | Vt_di_sp advP
    
    VP_simple -> V_mono_Adv NP_o conj S | V_mono_Adv conj S
    VP_simple -> V_be NP_o | V_be PP | V_be AdvP PP



NPrp -> 'Nadia' | 'Ross' | 'Marseilles' | 'Google'


N -> 'fur' | 'cat' | 'eggplant' | 'rutabaga' | 'boat' | 'poodle' | 'autoclave' | 'cloth' | 'cheese' | 'man' | 'elephant' | 'hovercraft' | 'autopoiesis' | 'help' | 'menu' | 'shoot' | 'demand' | 'reward'


Vi -> 'demand' | 'win' | 'believe' | 'jump' | 'shoot' | 'aspire' | 'help' | 'boat' | 'leave' | 'eat' | 'arrive' | 'see' | 'want'            
Vi_sp -> 'demanded' | 'won' | 'believed' | 'jumped' | 'shot' | 'aspired' | 'helped'| 'boated' |'left' | 'ate' | 'arrived' | 'saw' | 'wanted'                
Vi_pp -> 'demanded' | 'won' | 'believed' | 'jumped' | 'shot' | 'aspired' | 'helped' | 'boated' | 'left' | 'eaten' | 'arrived' | 'seen' | 'wanted'                   
Vi_pg -> 'demanding' | 'winning' | 'believing' | 'jumping' | 'shooting' | 'aspiring' | 'helping' | 'boating' | 'leaving' | 'eating' | 'arriving' | 'seeing' | 'wanting'


Vt_mono -> 'reward' | 'demand' | 'find' | 'give' | 'remind' | 'want' | 'win' | 'believe' | 'jump' | 'tell' | 'bring' | 'fondle' | 'shoot' | 'leave' | 'have' | 'help' | 'eat' | 'boat' | 'see'
Vt_mono_sp -> 'rewarded' | 'demanded' | 'found' | 'gave' | 'reminded' | 'wanted' | 'won' | 'believed' | 'jumped' | 'told' | 'brought' | 'fondled' | 'shot' | 'left' | 'had' | 'helped' | 'ate' | 'boated' | 'saw'
Vt_mono_pp -> 'rewarded' | 'demanded' | 'found' | 'given' | 'reminded' | 'wanted' | 'won' | 'believed' | 'jumped' | 'told' | 'brought' | 'fondled' | 'shot' | 'left' | 'having' | 'helped' | 'eaten' | 'boated' | 'seen'


Vt_di -> 'demand' | 'give' | 'remind' | 'tell' | 'bring' | 'reward'
Vt_di_sp -> 'demanded' | 'gave' | 'reminded' | 'told' | 'brought' | 'rewarded'
Vt_di_pp -> 'demanded' | 'given' | 'reminded' | 'told' | 'brought' | 'rewarded'


Aux_modal -> 'can' | 'may' | 'could' | 'should' | 'might' | 'must' | 'would' | 'will'
Aux_have_pres -> 'have' | 'has'
Aux_have_past -> 'had'
Aux_have -> 'have'

Aux_be_passive -> 'are' | 'were' | 'is' | 'was' | 'am'
Aux_be_past -> 'been'
Aux_be_pres -> 'be'
Aux_be_prog -> 'being'


P -> 'with' | 'in' | 'on' | 'by' | 'after' | 'before' | 'from' | 'of' | 'to' | 'onto' | 'for'


Adv -> 'immediately' | 'slowly' | 'already' | 'always' | 'really' | 'extremely' | 'often'


Adj -> 'long' | 'soft' | 'tall' | 'handsome'


Det -> 'the' | 'a' | 'an' | 'her' | 'my' | 'your' | 'his' | 'their' | 'that'


Pron_n -> 'I' | 'he' | 'she' | 'it' | 'we' | 'they' | 'you'


Pron_o -> 'me' | 'him' | 'her' | 'us' | 'them' | 'you'


V_to -> 'to'


conj -> 'that' | 'before' | 'after'


V_be -> 'are' | 'were' | 'is' | 'was' | 'am' 
                         
""")

a2_test = """Nadia left immediately
the cat with the long soft fur ate slowly with Nadia
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
Nadia arrived with her long cat
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
the long eggplant have been being eaten by Nadia
Nadia ate
Nadia slowly ate
Nadia ate slowly
Nadia ate slowly with cat
Nadia ate with cat slowly
Nadia ate slowly with the long soft cat
Nadia ate with the long soft cat slowly
Nadia ate with the cat with long soft fur
Nadia ate slowly with the cat with long soft fur
Nadia ate with the cat with long soft fur slowly
Nadia was eating
Nadia was slowly eating
Nadia was eating slowly
Nadia was slowly eating with cat
Nadia was slowly eating with her cat
Nadia was eating slowly with her cat
Nadia was eating with her cat with long soft fur slowly
Nadia was slowly eating with her cat with long soft fur
Ross is eating with her cat
Ross is eating with her cat on the hovercraft
Ross is eating with her cat on the hovercraft slowly
Ross is slowly eating with her cat on the hovercraft
she has left
she has left slowly
she has slowly left
she has left with the cheese
she has left with the cheese slowly
she has slowly left with the cheese
Nadia has left
Nadia has left from her
Nadia has left from her to the hovercraft
Nadia has slowly left from the cat on the hovercraft
he will leave
he will leave slowly
he will slowly leave
he will leave to the hovercraft
he will leave from her cat
she has been eating
she has been slowly eating
she has been eating slowly
she has been eating with her cat slowly
she has been slowly eating with her cat
she has been being helped
she has been being helped often
she has often been being helped
she has been being helped with her cat
she has been being helped with her cat with long soft fur
she has been being helped with her cat with long soft fur often
she has always been being helped with her cat
the cat with the long soft fur have been eating
the cat with the long soft fur have been slowly eating
the cat with the long soft fur have been eating slowly with Ross
Ross will have been eating
Ross will have slowly been eating
Ross will have been eating slowly
Ross will have been eating with Nadia slowly
Ross will have been eating with her cat with long soft fur
Nadia will have left
Nadia will have slowly left
Nadia will have left slowly
Nadia will have left slowly with her cat
Nadia will have left slowly with her cat with long soft fur
Nadia will have left slowly with her cat with long soft fur slowly
he will be eating
he will slowly be eating
he will be eating slowly
he will be slowly eating
he will be eating with her cat
he will be eating with her cat slowly
he will be eating with her cat with long soft fur slowly
Nadia is seen by her cat
Nadia was seen by her cat
Nadia was seen by her cat often
Nadia was often seen by her cat with long soft fur
the cat with long soft fur was helped by Nadia
the cat with long soft fur was often helped by Nadia
the cat with long soft fur is often helped by Nadia
Ross had been eaten slowly by the elephant
Ross had been slowly eaten by the elephant
Ross had been eaten slowly by the elephant with long soft fur
Ross had been eaten by the elephant with long soft fur slowly
the elephant will be seen by Ross
the elephant will often be seen by Ross
the elephant will be often seen by Ross
the elephant will be seen by Ross often
Nadia had left
Nadia had left immediately
Nadia had left with the elephant on the hovercraft
the tall elephant will have been being seen by Ross
the tall elephant will have been often being seen by Ross
the tall elephant will have been being seen often by Ross
the tall elephant will have been being seen by Ross on the hovercraft
the soft cat had eaten
the soft cat had eaten with Nadia
the soft cat had slowly eaten with Nadia
the soft cat had eaten slowly with Nadia on the hovercraft with Ross
Nadia saw Ross
Nadia shot Ross slowly
the cat had fur
the cat had long soft fur
Nadia saw the cat with long soft fur
Nadia had her help
Nadia had her help immediately
Nadia immediately had her help
the long cat brought Ross to the tall hovercraft
the cat believed that Ross was on the hovercraft
the long cat believed that Ross was on the hovercraft
the long soft cat believed that Ross was on the hovercraft with Nadia
the long soft cat believed that Ross was always on the hovercraft with Nadia
the long soft cat always believed that Ross was always on the hovercraft with Nadia
the long soft cat always believed that Ross was always on the hovercraft with Nadia always
Nadia was always with Ross
Nadia was always with the cat
Nadia was always with the cat with long soft fur
Nadia rewarded Ross the long soft cat
Nadia rewarded Ross the long soft cat with her elephant
Nadia helped Ross with long soft cat on the hovercraft
Nadia immediately helped Ross with long soft cat on the hovercraft
Nadia reminded Ross of the cat with long soft fur
Nadia reminded Ross of the cat with long soft fur of her
Nadia brought Ross for the cat
Nadia brought the tall elephant to the hovercraft
Nadia brought the tall elephant of Ross to the hovercraft
Nadia brought the tall elephant of Ross to the hovercraft for the cat
Ross reminded Nadia that she saw the cat
Ross often reminded Nadia that she saw the cat
Ross reminded Nadia that she saw the cat often
Ross believed that she saw the cat
Ross often believed that she saw the cat
Ross believed that she saw the cat often
Ross gave the cat an elephant on the hovercraft
Ross immediately gave the cat an elephant on the hovercraft
Ross gave the cat an elephant on the hovercraft immediately
the cat with long soft fur left
a tall elephant ate
a cat immediately left
my soft soft cat jumped slowly
Nadia will leave
Nadia has left
Nadia may have been leaving
Ross is eaten
Ross is eating
Ross is being eaten
Ross has eaten
Ross has been eaten
Ross has been eating
Ross has been being eaten
Ross will eat
Ross will be eaten
Ross will be eating
Ross will be being eaten
Ross will have eaten
Ross will have been eaten
Ross will have been eating
Ross will have been being eaten
she has been being found
Ross ate the soft cheese
she gave me a cat
I gave him a cat with long soft fur
I brought a cat with long soft fur
I told him me
Nadia fondled the soft eggplant
Nadia ate slowly
she was left
she was left on the hovercraft
she was immediately left on the hovercraft
the cat is eating with the eggplant
the cat is always eating with the eggplant with the long soft fur
the cat is eating
the cat was eating
the cat is being eaten
the cat is being eaten by Nadia
the cat was being eaten by Nadia
the eggplant left immediately 
the eggplant left with Nadia
the eggplant left immediately with Nadia
the eggplant left with the cat onto Nadia
the eggplant left with the cat onto Nadia immediately 
the eggplant left the cat
the eggplant left the cat with the long soft fur
the eggplant left the cat immediately
she had left
she had left with the cat with long soft fur
she had left immediately
she had left with the cat with long soft fur immediately
she had already left
she has left
she has left immediately
she has already left
she has been eaten
she has been eating
she had been eating
she had been eaten
she has been eaten by the cat
Nadia left
the cat with long soft fur slowly ate
the cat with long soft fur ate slowly
the long soft fur cat immediately left
the long soft fur cat left immediately
Nadia left with the cat with the long soft fur
Nadia left
Nadia immediately left
Nadia left immediately
the cat was eaten
the cat was slowly eaten 
the cat was eaten slowly
the cat was eaten by Nadia
Nadia was eating
Nadia was slowly eating
Nadia was eating slowly
Nadia was being eaten
the cat was being eaten by Nadia
Nadia had arrived
the long fur cat had been eaten
the long fur cat had been eaten by Nadia
Nadia had already arrived
Nadia had arrived already
the long fur cat with Nadia had arrived
the long fur cat had been eating
the long fur cat had been slowly eating
the long fur cat had been eating slowly
Nadia had been leaving
Nadia had been leaving with the long fur cat
the long fur cat had slowly been eating
the long fur cat with the handsome man had been leaving
the long fur cat had been slowly eating by the handsome man
the long fur cat had been being eaten
the long fur cat had been slowly being eaten
the long fur cat had been slowly being eaten by the handsome man
the long fur cat had slowly been being eaten
the long fur cat had been being eaten slowly
Nadia had been leaving
Nadia had been leaving with the long fur cat
the long fur cat with the handsome man had been leaving
the long fur cat had been being eaten
the long fur cat had been slowly being eaten
the long fur cat had slowly been being eaten by the handsome man
the long fur cat had slowly been being eaten
the long fur cat had been being eaten slowly
Nadia had been leaving
Nadia had been leaving with the long fur cat
the long fur cat with the handsome man had been leaving
the long fur cat had been being slowly eaten
the long fur cat is eaten
the cat is slowly eaten 
the cat is eaten slowly
the cat is eaten by Nadia 
the cat with long fur is eaten by Nadia
the long fur cat is being eaten
the cat is slowly being eaten 
the cat is being eaten slowly by Nadia
Nadia is leaving
Nadia is immediately leaving
Nadia is leaving immediately
the long fur cat has been eaten
the long fur cat has slowly been eaten
the long fur cat has been slowly eaten
the long fur cat has been eaten slowly by Nadia
Nadia has left
Nadia has immediately left
Nadia has left immediately with her long fur cat
the long fur cat has been being eaten
the long fur cat has slowly been being eaten
the long fur cat has been slowly being eaten
the long fur cat has been being slowly eaten
the long fur cat has been being eaten slowly by Nadia
the long fur cat has been being eaten
the long fur cat has slowly been being eaten
the long fur cat has been slowly being eaten
the long fur cat has been being slowly eaten
the long fur cat has been being eaten slowly by Nadia
Nadia has been leaving
Nadia has immediately been leaving
Nadia has been immediately leaving
Nadia has been leaving immediately
the long fur cat will be eaten
the long fur cat will slowly be eaten
the long fur cat will be slowly eaten
the cat with long fur will be eaten slowly by Nadia
the handsome man will leave
the handsome man will immediately leave with his cat
the long fur cat will be eaten
the long fur cat will slowly be eaten
the long fur cat will be slowly eaten
the cat with long fur will be eaten slowly by Nadia
the handsome man will leave
the handsome man will immediately leave with his cat
the handsome man with his cat will leave immediately
the long fur cat will be being eaten
the cat with long fur will slowly be being eaten
the cat with long fur will be slowly being eaten by Nadia
the handsome man will be leaving 
the handsome man will be immediately leaving with his cat
the long fur cat will have been eaten
the cat with long fur will have slowly been eaten by handsome man
the handsome man will have left
the handsome man will have immediately left
the long fur cat will have been being eaten
the cat with long fur will have been being eaten by Nadia
the handsome man will have been leaving
the handsome man will have been leaving immediately
the long fur cat would be eaten
the long fur cat would be eaten slowly by Nadia
the handsome man would leave immediately
the handsome man with his cat would immediately leave
the cat with long fur would be being eaten
the long fur cat would be being eaten slowly
the handsome man would be leaving immediately with his cat
the handsome man would be immediately leaving with him
the cat would have been eaten
the cat with long fur would have been eaten slowly by Nadia
the handsome man with his cat would have left
the handsome man would have arrived with Ross
the long fur cat would have been being eaten
the cat with long fur would have been being eaten by Nadia
the handsome man with his cat would have been leaving
the handsome man would have been leaving immediately with his cat
I had to help
he had to help Nadia
they told her to jump onto the elephant
the handsome poodle brought Ross to the autoclave
the handsome man told her to jump onto the elephant
Nadia believed that Ross was already on the hovercraft
she believed that Ross was on the hovercraft already
Nadia brought a cloth for the cheese
Nadia was always with Ross
Nadia was always with her cat with long fur
the handsome man gave the cat the eggplant
Nadia told her cat the autopoiesis
she told me that Ross was on the hovercraft
Nadia really wanted to help
she always believed that they brought a cloth for the cheese
she always believed before they brought a cloth for the cheese
Nadia really wanted to jump
they told her to jump onto the elephant
the cat to help slowly ate
Nadia saw the cat jumping
Nadia saw the cat eat
Nadia was leaving
Nadia was slowly leaving
Nadia was leaving slowly
she really aspired to help
Nadia has eaten the eggplant
she will help Nadia
Nadia believed that Ross was already on the hovercraft
she believed that Ross was on the hovercraft already
she believed that they brought a cloth for the cheese
she told me that Ross was on the hovercraft
she always believed that they brought a cloth for the cheese
she always believed before they brought a cloth for the cheese
they brought a cloth for the cat
she always believed that they brought a cloth for the cat
she always believed before they brought a cloth for the cat
Nadia left immediately
the cat with the long soft fur slowly ate
she arrived
Nadia will leave
Nadia has left
Nadia may have been leaving
Nadia fondled the eggplant
the handsome poodle brought Ross to the autoclave
Nadia brought a cloth for the cheese
they told her to jump onto the elephant
she believed that Ross was already on the hovercraft
she really wanted help
she really aspired to help
cheese was always on the menu
the eggplant reminded Nadia of Ross
she reminded the handsome man to eat the elephant
Nadia fondled the eggplant
the handsome poodle brought Ross to the autoclave
Nadia brought a cloth for the cheese
they told her to jump onto the elephant
she believed that Ross was already on the hovercraft
she really wanted help
she really aspired to help
cheese was always on the menu
the eggplant reminded Nadia of Ross
Nadia really wanted to jump
I had cheese for eating"""


a3_test = """
Nadia with the long soft fur slowly ate
Nadia with the long soft fur slowly ate
Nadia will left
Nadia really wanted to jump
Ross brought to him
I had cheese for eating
I had cheese for eating
they told to jump onto the elephant
Nadia found
Nadia has could leave
Nadia has had left
they gave for the cat
Nadia found
Ross brought to him
they told to jump onto the elephant
her arrived with her cat
the the cat arrived 
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
Nadia has will immediately left
Nadia has could left
Nadia could has left
Nadia will ate
Nadia is arrived
Ross is is eaten
Ross have be seen with Nadia
Ross have being seen with Nadia
Ross will has being seen with Nadia
the cat has has arrived
the cat have have arrived
the cat had had arrived
the cat will is being seen
the cat will being is seen
the eggplant may be is eating
the eggplant may is being seen
Nadia already had been eating with her cat
Ross already has been seen
she often will jumped
Nadia will have been jump
Nadia may is eating
Nadia may is eaten
Nadia may is eaten
Ross may have been eat
Ross may have be eating
the soft cat have had been eating
the soft cat have has been eating
the soft cat have had be eating
Nadia has could left
Nadia could has left
Nadia will ate
Nadia is arrived
Ross is is eaten
Ross have be seen with Nadia
Ross have being seen with Nadia
Ross will has being seen with Nadia
the cat has has arrived
the cat have have arrived
the cat had had arrived
the cat will is being seen
the cat will being is seen
the eggplant may be is eating
the eggplant may is being seen
Nadia already had been eating with her cat
Ross already has been seen
she often will jumped
Nadia will have been jump
Nadia may is eating
Nadia may is eaten
Nadia may is eaten
Ross may have been eat
Ross may have be eating
the soft cat have had been eating
the soft cat have has been eating
the soft cat have had be eating
the soft long cat eating immediately with Ross
the soft long cat eaten immediately with Ross
Ross with the long soft fur ate slowly with Nadia
Nadia with the long soft fur ate slowly with Ross
the elephant had eat with the cat
the elephant had eating with the cat
the elephant has will leave
the elephant had will leave
the elephant have will left immediately
the elephant is eat
the elephant eat is
Nadia left handsome
Nadia leave handsome
Nadia handsome leave slowly
the eggplant is having being seen
her arrived with the long soft fur
I with the tall you arrived
Nadia has eating
Ross could ate
Nadia must has been eaten
Nadia must have be eaten
the handsome she arrived
she was helping the cat
she was slowly helping the cat
she was helping immediately the cat
she was slowly helping the cat with the long soft fur
the cat was eating the eggplant
handsome she arrived
she arrived handsome
the Nadia arrived
her arrived with Nadia
Nadia with the long soft fur slowly ate
you with the long soft fur slowly ate
the cat was arrived
Nadia will eating with his cat
Nadia could has left
Nadia has would leave
Nadia has had left
Nadia was arrived
Nadia had will leave
the cat is will eat
the cat was has eaten
the long fur cat have had being eaten
the soft man have will eating
Nadia should was eating
Nadia may been arrived
Ross would is been eaten
the long fur cat
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
Nadia has eating
Ross could ate
Nadia must has been eaten
Nadia must have be eaten
Nadia gave
the cat had 
the handsome man brought to me
the handsome man arrived the boat
the man win the boat a cat
Nadia gave
the cat had 
the handsome man brought to me
they gave for the cat 
the handsome man arrived the boat
the man win the boat a cat
the slowly cat arrived
the cat soft ate
Nadia found
Ross brought to him
they told to jump onto the elephant
Nadia will has left
I had cheese for eating"""

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

count1 = 0
a3_test_list = [s.split() for s in a3_test.split('\n')]
for s in a3_test_list:
    try:
        #print("==========================")
        if len(list(parser.parse(s))) > 0:
            count1 += 1
            words = ' '.join(s)
            print(words)
        # print(len(list(parser.parse(s))) > 0)
    except Exception as e:
        print(e)
print(count1)

sent = ["the handsome poodle brought Ross to the autoclave",
        "they told her to jump onto the elephant",
        "she believed that Ross was already on the hovercraft",
        "she really wanted help",
        "she really aspired to help",
        "cheese was always on the menu",
        "the eggplant reminded Nadia of Ross",
        "Nadia found",
        "Ross brought to him",
        "they wanted to jump onto the elephant",
        "they gave the long fur cat the long fur cat with the long fur cat",
        "Nadia shot Ross slowly",
        "I had cheese for eating"]

for tree in parser.parse(sent[12].split()):
    #print(tree)
    tree.draw()