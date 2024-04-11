def rps(Naruto,Kurama):
    if Naruto == Kurama:
        return "It's die"
    if Naruto == 'rock' and Kurama == 'scissors' or Naruto == 'paper' and Kurama == 'rock' or Naruto == 'scissors' and Kurama == 'paper':
        return "Naruto Wins"
    else:
        return "Kurama Wins"
def calwin():
    print("Welcome tp rps game da bois!")
    Naruto=input("Naruto,Enter your value:")
    Kurama=input("Kurama,Enter your value:")
    while Naruto not in ['rock','scissors','paper'] or Kurama not in ['rock','scissors','paper']:
        print("Invalid.Enter your value again('rock','scissors' or 'paper')")
        Naruto=input("Naruto,Enter your value:")
        Kurama=input("Kurama,Enter your value:")
    print(rps(Naruto,Kurama))
calwin()
        
    
