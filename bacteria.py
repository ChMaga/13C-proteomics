from reframed import FBA
from reframed import load_cbmodel,save_cbmodel,Metabolite, Environment

bacteria = load_cbmodel('C:/Users/bacteria.xml', flavor='cobra')   

metabolite1= Metabolite('M_cit_e','Citrate','C_e')
bacteria.add_metabolite(metabolite1)
bacteria.add_reaction_from_str('R_EX_cit_e: M_cit_e <->  [-1000, 1000]')

metabolite2= Metabolite('M_gal_e','Galactose','C_e')
bacteria.add_metabolite(metabolite2)
bacteria.add_reaction_from_str('R_EX_gal_e: M_gal_e <->  [-1000, 1000]')


bacteria.add_reaction_from_str('R_GALt2: M_gal_e + 2 M_h_e <-> M_gal_c + 2 M_h_c [-1000, 1000]')
bacteria.add_reaction_from_str('R_LCTSt: M_h_e + M_lcts_e <-> M_h_c + M_lcts_c [-1000, 1000]')
bacteria.add_reaction_from_str('R_LCTStex: M_lcts_e <-> M_lcts_p [-1000, 1000]')


bacteria.remove_reactions(['R_ALATA_L','R_SDPTA','R_TKT2','R_GLUSy','R_ARGDr','R_ASNN']) 
bacteria.add_reaction_from_str('R_ALATA_L: M_pyr_c + M_glu__L_c --> M_akg_c + M_ala__L_c [0, 1000]')#based on Ponomarova O, et al., 2017
bacteria.add_reaction_from_str('R_SDPTA: M_sl26da_c --> M_sl2a6o_c + M_nh4_c [0, 1000]')#based on Ponomarova O, et al., 2017
bacteria.add_reaction_from_str('R_TKT2: M_f6p_c + M_g3p_c --> M_xu5p__D_c + M_e4p_c [0, 1000]')#based on Ponomarova O, et al., 2017

save_cbmodel(bacteria, 'bacteria_new.xml', flavor='cobra')

medium ={'cl','ribflv','thm','iodine','4abz','arg__L','asn__L','btn','ca2','cobalt2','cu2','fe2',
        'fe3','fol','gthrd','his__L','ile__L','leu__L','met__L','inost','k','mg2','mn2',
        'nac','pi','pydxn','tyr__L','val__L','zn2','so4','pnto__R','feenter','lcts'
       ,'ala__L','asp__L','glu__L','gly', 'gln__L','ser__L','thr__L'}


Environment.from_compounds(medium).apply(bacteria, inplace=True)
solution = FBA(bacteria)
print (solution)
