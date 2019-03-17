with open('referat.txt', 'r', encoding='utf-8') as f:
    ref = f.read()
    print(len(ref))

with open('referat.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        ln = ln.replace('.', '!')
        with open('referat2.txt', 'a', encoding='utf-8') as newfile:
            newfile.write(ln)
  
   

