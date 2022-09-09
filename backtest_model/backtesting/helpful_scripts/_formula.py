
def making_formula(formula,made_string=""):
    print(formula)
    for key,value in formula.items():

        if 'C' in key:
            if value=="None":
                made_string=made_string+key

            else:
                made_string=made_string+'('+key + ' '  +value['operator']+' '

                formulas={
                    list(formula[key].keys())[1]:list(formula[key].values())[1]
                }
                print(formulas)
                made_string=making_formula(formulas,made_string)
                made_string=made_string+')'
        else:
            made_string=made_string + ' ' + value +' '
    return made_string
