from reframed import load_cbmodel,save_cbmodel,Environment,FBA,Community,Metabolite,Gene
yeast = load_cbmodel('C:/Users/yeast.xml', flavor='cobra')


new_gene = Gene('PUT2', 'PUT2')
yeast.add_gene(new_gene)
new_gene1 = Gene('GLN1', 'GLN1')
yeast.add_gene(new_gene1)

yeast.add_reaction_from_str('R_GDH1: M_glu__L_c + M_h2o_c + M_nad_c <-> M_akg_c + 2 M_h_c + M_nadh_c + M_nh3_c [-1000,1000]') 
yeast.add_reaction_from_str('R_GLUDy_1: M_glu__L_c + M_h2o_c + M_nadp_c <-> M_akg_c + 2 M_h_c  + M_nadph_c + M_nh3_c [-1000,1000]') 
yeast.add_reaction_from_str('R_P5CD: M_1pyr5c_c + 2  M_h2o_c +  M_nad_c <-> M_glu__L_c + M_h_c +  M_nadh_c[-1000,1000]')
yeast.add_reaction_from_str('R_GLNS_1:  M_atp_c + M_glu__L_c + M_nh3_c <-> M_adp_c + M_gln__L_c + M_pi_c[-1000,1000]')
                    
yeast.add_reaction_from_str('R_GDH2: M_nadp_c + M_glc__bD_c <-> M_h_c + M_nadph_c + M_15gl_c [-1000,1000]')
yeast.add_reaction_from_str('LDH_D:M_lac__D_c + M_nad_c <-> M_h_c + M_nadh_c + M_pyr_c[-1000,1000]')                 
yeast.add_reaction_from_str('R_EX_gln__L_e: M_gln__L_e <->  [-1000, 1000]')
yeast.add_reaction_from_str('R_DAPDC: M_26dap__M_c + M_h_c <-> M_co2_c + M_lys__L_c [0,1000]')  
yeast.add_reaction_from_str('R_EX_lcts_e:M_lcts_e<->  [-1000, 1000]')

metabolite1= Metabolite('M_lcts_e','Lactose','C_e')
yeast.add_metabolite(metabolite1)


save_cbmodel(yeast, 'yeast_new.xml', flavor='cobra')

medium ={'cl','ribflv','thm','iodine','4abz','arg__L','asn__L','btn','ca2','cobalt2','cu2','fe2',
        'fe3','fol','gthrd','his__L','ile__L','leu__L','met__L','inost','k','mg2','mn2',
        'nac','pi','pydxn','tyr__L','val__L','zn2','so4','pnto__R','feenter','glc__D'}

Environment.from_compounds(medium).apply(yeast)
solution = FBA(yeast)
print (solution)

solution2 = FBA(yeast, constraints={'R_GALt2':0})
print (solution2)

