para=input("Enter the Sentence or Paragraph here: ")
s_para=para.split()
for i in s_para:
    def wrd_cnt(p):
        c=0
        for i in p:
            c += 1
        return c
count=wrd_cnt(s_para)
print(f"There are {count} number of words in the given word file.")
