print('A Morse Code translator!')
print('Use "Morse: " before Morse code to translate Morse code into English')
print('Use "English: " before English to translate into Morse code')
print('Python interpreter works as usual otherwise')

Morse_English = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-..':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '   ':' ', '--..--':',', '.-.-.-':'.', '..--..':'?', '---...':':', '.-..-.':'"'}

English_Morse = dict(zip(list(Morse_English.values()), list(Morse_English.keys())))

def Morse(x):
    x += ' '
    for a in x:
        if a != '-' and a != '.' and a != ' ':
            return "Input must be Morse Code"
    letters = ''
    letter = ''
    for a in x:
        if a != ' ':
            letter += a 
        else:
            if letter not in Morse_English:
                return '"' + letter + '"' + " not translatable"
            letters += Morse_English[letter]
            letter = ''
    return letters

def English(x):
    x += ' '
    translation = ''
    for a in x:
        if a not in list(English_Morse.keys()):
            return "Untranslatable character " + '"' + a + '"'
    for a in x:
        translation += English_Morse[a]
        translation += ' '
    return translation

while True:
    x = input(">>> ")
    if x[0:6] == 'Morse:':
        print(Morse(x[7:]))
    elif x[0:8] == 'English:':
        print(English(x[9:]))
    else:
        print(eval(x))