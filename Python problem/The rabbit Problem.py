# Problem Statement:
# Start with 1 pair of rabbits.
# Each pair becomes fertile after 1 month.
# Every fertile pair produces 1 new pair per month.
#Rabbits never die.
#after 12 month how many rabbit pair

def rabbit(m):
    if m==0 or m==1:
        return 1
    else:
        return rabbit(m-1)+rabbit(m-2)
print(rabbit(12))