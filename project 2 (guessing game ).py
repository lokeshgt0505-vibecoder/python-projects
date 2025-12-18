secret_number=9
guess_count: int=0
guess_limit=2
while guess_count < guess_limit:
    guess_count += 1
    guess=int(input("enter your guess:"))
    if guess==secret_number:
        print ("you won you fellaw !!!!!")
        break
else:
    print("sorry you failed you dumb")
