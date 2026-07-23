s = 'Hello Mr. Rogers, how are you this Day?'
def up_low(string):
    uppercase = 0
    lowercase = 0
    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'Original string: {string}')
    print(f'Number of uppercase characters: {uppercase}')
    print(f'Number of lowercase characters: {lowercase}')
up_low(s)