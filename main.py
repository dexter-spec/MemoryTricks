import ast
def red():
    with open("assts.txt","r+") as f:
        lol = f.read()
        
        return lol


def write(initial, value):
    with open("assts.txt","r+") as f:
        lol = f.read()
        res = ast.literal_eval(lol)
        res.update({initial:value})
        res = str(res)
    with open("assts.txt","w+") as f:
        f.write(res)
new_list = []
n_list=[]
def take():
    key = input("keywords: ")
    ress= key.split(",")
    lma = red()
    lmao = ast.literal_eval(lma)
    for x in ress:
        try:
            d = lmao[x]
            new_list.append(d)
            dm = f"{x}({d})"
            n_list.append(dm)
            
        except:
            tk = input(f":::{x}:::not found give me the word: ")
            write(x,tk)
            d = tk
            new_list.append(d)
            dm = f"{x}({d})"
            n_list.append(dm)
    return new_list, n_list
            
        
            
        
    

x,y = take()
print(x)
print(y)
