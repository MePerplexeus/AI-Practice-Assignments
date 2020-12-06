while True:
        try:
            inp = int(input("Enter an integer between 1 to 10: "))
            if inp >= 1 and inp <= 10:
                print('The Reciprocal of your number is',str(1/inp)+'.')
                break
            else:
                if inp > 10 or inp < 0:
                    print('You did not enter a number between 1 and 10!!!')
                    print('Please, try again.\n')
                elif inp == 0:
                    print('Oops, you entered zero.')
                    print('Please, try again.\n')
        except:    
            print('You did not enter an integer!!!')
            print('Please, try again.\n')