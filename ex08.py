n = int(input())
galleons = n // (17 * 29)
sickles = (n % (17 * 29)) // 29
knuts = (n % (17 * 29)) % 29

if galleons > 0:
    print(f"{galleons} галлеонов")
if sickles > 0:
    print(f"{sickles} сиклей")
if knuts > 0:
    print(f"{knuts} кнатов")
