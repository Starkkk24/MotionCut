file=input("Enter the name of the .txt file: ")
f=open(f"{file}.txt","r")
para=f.read().splitlines()
for i in para:
    s_para=i.split()
def wrd_cnt(p):
    c=0
    for i in p:
        c += 1
    return c
count=wrd_cnt(s_para)
print(f"There are {count} number of words in the given word file.")
