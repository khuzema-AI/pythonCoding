print ('Hy!')

print ('Its Maths Game!')

def mathGame():
    A1 = 4+4

    answer = input("You in?")

    if answer == 'yes' or 'yeah' :
        print ('good!')
        print ('Challenge 1')
        Q1 = int(input('Q1: 4+4=?'))
        
        if Q1==A1:
            print ('Correct!')
        else:
            print ('Nopes Try Next Time!')

    else:
        print ('Its okay, Bye')

mathGame()








    


