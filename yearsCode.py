import random, re

def calc(year):
    return (year // 12 + year % 12 % 7 + year % 12 // 4) % 7

def getYearCodeDict(minRange, maxRange):
    return { r: calc(r) for r in range(minRange, maxRange + 1) }

minRange, maxRange = 60, 70
yearcode = getYearCodeDict(minRange, maxRange)
checkAsnwers = []

def main():
    while True:
        ask = [random.randint(minRange, maxRange) for _ in range(10)]
        print(ask)

        answer = list(map(int, re.split(r"\s+", input().strip())))
        checkAnswers = [a == an for a, an in zip(map(calc, ask), answer)]

        # print(checkAnswers)
        # print([yearcode[a] == a for a, an in zip(ask, answer)])
        # print(list(map(calc, ask)))
        
        printList = [ask, answer, ["True" if c else "False" for c in checkAnswers], list(map(calc, ask))]
        
        # printWidth = max(map(lambda x: len(str(x)), [k for p in printList for k in p]))
        printWidth = max([max(map(lambda x: len(str(x)), p)) for p in printList]) + 1

        for z in printList:
            print(("{:{align}{width}} " * len(z)).format(*z, align="^", width=printWidth))

        # print(("{:<6} " * len(checkAnswers)).format(*["True" if c else "False" for c in checkAnswers]))
        # print(("{:<6} " * len(list(map(calc, ask)))).format(*list(map(calc, ask))))

        print()

        for p in zip(*[z for z in zip(*printList) if z[2] == "False"]):
            print(("{:{align}{width}} " * len(p)).format(*p, align="^", width=6))

        if not all(checkAnswers):
            print(yearcode)
        # print()
        # ask = random.randint(0, 50)
        #print(int(input(str(ask) + " = ")) == calc(ask), calc(ask))

if __name__ == "__main__":
    main()