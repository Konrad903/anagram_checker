class anagram:
    def __init__(self):
        self.str1=str(input('Enter first word: '))
        self.str2=str(input('Enter second word: '))

    def display(self):
        if sorted(self.str1)==sorted(self.str2):
            print('The strings are an anagram')
        else:
            print('The strings are not an anagram')

a=anagram()
a.display()

