import random

lottoOfThisWeek = []
while len(lottoOfThisWeek) < 6:
    num = random.randint(1, 45)
    if num not in lottoOfThisWeek:
        lottoOfThisWeek.append(num)

lottoOfThisWeek.sort()
print(lottoOfThisWeek)
