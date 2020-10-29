from reframed import load_cbmodel,FBA
community = load_cbmodel('C:/Users/magantev/Desktop/fasta2/community.xml', flavor='cobra')


#Medium can be further modified by adding/excluding lcts=lactose, glc__D=glucose, gal=galactose
medium ={'cl','ribflv','thm','iodine','4abz','arg__L','asn__L','btn','ca2','cobalt2','cu2','fe2',
        'fe3','fol','gthrd','his__L','ile__L','leu__L','met__L','inost','k','mg2','mn2',
        'nac','pi','pydxn','tyr__L','val__L','zn2','so4','pnto__R','feenter','lcts'
        'ala__L','asp__L','glu__L','gly', 'gln__L','ser__L','thr__L'}


Environment.from_compounds(medium).apply(community)
solution = FBA(community)
print (solution)


solution = FBA(community, constraints={'R_GALt2_cremoris_ref2':0,'R_GALt2_yeast_LB':0})
print (solution)
