items = ["bun dau","bun bo","bun rieu"]
print(items[-1])
print(*items, sep=",") # them * trc de bo di dau [] va dau nhay don 

n = input("ban muon dung them mon nao ?")
items.append(n)
print(*items, sep=",") # sep = "," de them dau phay sau moi mon


