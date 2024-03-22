pin = input()
p = str(pin)
if (len(pin) == 4 and not 1900 <= int(pin) <= 2050 and p[0] != p[1] and p[0] != p[2]
        and p[0] != p[3] and p[1] != p[2] and p[1] != p[3] and p[2] != p[3]):
    print('OK')
else:
    print('ERROR')
