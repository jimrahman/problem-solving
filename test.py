data = "mom"

def palendrom(name):
    reverseName = ''
    for i in range(len(data)):
        reverseName += data[-i-1].upper()

    if name.upper() == reverseName.upper():
        print("palendromic")
    else: print("Not palendromic")


 


data = "mom"

unique = set(data)
unique.update("dog", "god")
print(unique)

name = ['Jim', 'Afsana', 'Pollob', 'Rony', 'Riyad', 'Benjamin', 'Sakib', 'Tokid', 'Misbah', 'Rakib']
Front_end = ['Jim', 'Benjamin', 'Rakib']
Back_end = ['Jim', 'Rakib']

not_developer = set(name).difference(Front_end, Back_end)
fullStack = set(Front_end).intersection(Back_end)
onlyFrotend = set(Front_end).difference(Back_end)

print(not_developer)
print(fullStack)
print(onlyFrotend)

