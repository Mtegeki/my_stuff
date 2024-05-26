c_poplation = {
    "china" : 1233,
    "tanzania" : 1542,
    "kenya" : 125,
    "uganada" : 1452
}

def add():
    pop_c = input("weka nchi ambayo ungetamani kuiongeza kwenye orodha: ")
    pop_c = pop_c.lower()
    if pop_c in c_poplation:
        print(f"unajaribu kuweka {pop_c} kwenye ambayo tiyali ipo")
        return
    pop_l = input(f"weka populatitioni iliyopo kwenye nchi ya {pop_c} : ")
    pop_l = float(pop_l)
    c_poplation[pop_c] = pop_l
    show_all()
def query():
    pop_c = input("weka jina la nchi ambayo ungetamani kuona taarifa zake : ")
    pop_c = pop_c.lower()
    if pop_c not in c_poplation:
        print(f"nchi {pop_c} unayojaribu kuweka taarifa zake hazipo kwenye database yetu")
        return
    print(f"nchi {pop_c} ina population ya {c_poplation[pop_c]}")
def remove():
    pop_c = input("weka jina lanchi ambayo ungetamani kuiondoa kwenye database yetu : ")
    pop_c = pop_c.lower()
    if pop_c not in c_poplation:
        print(f"unajaribu kufuta {pop_c} ambayo haipo kwenye database yetu")
        return
    del c_poplation[pop_c]
    print(f"{pop_c} imefutwa kikamilifu")
    show_all()
    
def show_all():
    for i, l in c_poplation.items():
        print(f"nchi ya {i} ina population ya watu {l}")

op = input("weka agizo unalotaka kufanya ('ongeza', 'futa', 'onesha moja', 'onesha zote')")
op = op.lower()
if op == "ongeza":
    add()
if op == "futa":
    remove()
if op == "onesha moja":
    query()
if op == "onesha zote":
    show_all()
