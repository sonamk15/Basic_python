a = [10,20,30,20,10,50,60,40,80,50,40]


uniq_items = []
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
        # dup_items.add(x)

# print(dup_items)
print(uniq_items)
