def hangman_check(character,private,public):
    """Checks if a character is in the private list and then repalces the one in the public if so"""
    for i in range(len(private)):
        if character == private[i]:
            public[i] = private[i]
    return character,private,public

def hangman():
    run = True
    guesslist = []
    private = [x.lower() for x in input('Give me a word!\n')]
    public = ['_' for x in private]
    for i in range(100):
        print('\n')
    while run:
        print(public,'\n',guesslist)
        guess = input('Input your character guess!\n').lower()
        rechar,private,public = hangman_check(guess,private,public)
        guesslist.append(rechar)
        if public == private:
            print('You win')
            run = False
        elif len(guesslist) == 10:
            print('You lose HAHAHAHHA loser')
            run = False

hangman()
