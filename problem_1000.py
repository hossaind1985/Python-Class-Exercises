
def indices(lis,trg):
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i] + lis[j] == trg:
                return [i,j]



lst = input("Enter a list with 'Comma(,)' in between:").split(',')
lis = [int(num) for num in lst ]
print(lis)
trg = int(input("Enter Your Target Number:"))

print(indices(lis,trg))