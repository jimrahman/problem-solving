
data1= "mom"
data2="dog"
data3= "tEnEt"


def palendrom(data):
    reverseData = ""

    for i in range(len(data)):
        reverseData += data[-i-1]

    if data.upper() == reverseData.upper():
        print("the word is palendromic")
    else:
        print("Not palendromic")






palendrom(data3)
palendrom(data2)
palendrom(data1)
