T = int(input())
for i in range(T):
    s = input()
    if s == 'B' or s == 'b':
        print('BattleShip')
    elif s == 'F' or s == 'f':
        print('Frigate')
    elif s == 'C' or s == 'c':
        print('Cruiser')
    else:
        print('Destroyer')
