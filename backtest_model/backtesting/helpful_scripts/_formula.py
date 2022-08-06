
# formula= {  "C1":{
#         "operator":'and',
#         "C2":{"operator":"or",
#             "C3":{"operator":"and",
#             "C8":None}}
#     },
#     "operator1":'or',
#     "C4":None,

#     "operator2":'and',
#     "C5":None,
# }

# formula={"C1":None}
# made_string=""
formula={"dicts['C1']": {"operator": "&", "dicts['C2']": "None"}}
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
print(making_formula(formula,""))
# if __name__=="__main__":
#     print(making_formula(formula,""))