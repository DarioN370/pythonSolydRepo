#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘.
#   >4999 = Silver
#   5000 > 9999 = Gold
#   10000 > 19999 = VeryGood Player
#   20000 > 24999 = Over Player
#   25000 > 29999 = Try hard Player
#   < 30000 = Pro player or HVH
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘.

print ('⫘⫘⫘⫘⫘CS2 RANKING CALCULATOR⫘⫘⫘⫘⫘')

while True:
    try:
        userRanking = int(input('Type your premier ranking: '))
        break
    except ValueError:
        print('❌ Please enter a valid ranking')
# Toda essa parte de cima cria um loop em caso de error, caso o user digite algo que não pode ser convertido para numero, o codigo fica mandando ele digitar um numero valido, e quando o codigo consegue converter, ele roda os ELIFs

if userRanking <= 4999:
    print('Silver, a bad or new player')
elif 5000 <= userRanking <= 9999:
    print('Gold Player, development new player')
elif 10000 <= userRanking <= 19999:
    print('VeryGood Player, a good and promise player')
elif 20000 <= userRanking <= 24999:
    print('Over Player, promise player')
elif 25000 <= userRanking <= 29999:
    print('Try hard Player')
elif userRanking > 30000:
    print('Pro player or HVH')
else:
    print('Sorry, no ranking')

print ('⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')