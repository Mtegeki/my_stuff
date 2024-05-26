import statistics

s_trike = {
    "january" : [3500,1500,200],
    "feb" : [4500,7500,800],
    "mach" : [3900,1600,700],
    "apr" : [2500,8500,280],
}
def print_all():
    for s, pr in s_trike.items():
        avg = statistics.mean(pr)
        print(f"{s} {pr} ===> avg :", round(avg))
def add():
    s = input("weka mwezi unaotaka kuweka taarifa zake: ")
    p = input("weka taarifa za mwezi huo: ")
    p = float(p)

    
    if s in s_trike:
        s_trike[s].append(p)
    else:
        s_trike[s] = [p]
    print_all()
def main():
    op = input("Enter opeation (add, print) : ")
    op = op.lower()
    if op == "add":
        add()
    elif op == "print":
        print_all()
    else:
        print(f"operation {op} is not surpoted") 

if __name__ == "__main__":
    main()