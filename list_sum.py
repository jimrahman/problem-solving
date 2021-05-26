l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

reverseList1 = ""
reverselist2 = ""

for i in range(len(l1)):
    strlist = str(l1[-i-1])
    reverseList1 += strlist

for i in range(len(l2)):
    strlist = str(l2[-i-1])
    reverselist2 += strlist

sum_reverse_l1_l2 = str(int(reverselist2) + int(reverseList1))
sum_reverse_list = []

for i in range(len(sum_reverse_l1_l2)):
    sum_reverse_list.append(sum_reverse_l1_l2[-i-1])

print(sum_reverse_list)




