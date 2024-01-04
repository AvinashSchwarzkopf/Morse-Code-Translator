print('A Morse Code translator!')
print('>>> Morse: .... . .-.. .-.. ---     .-- --- .-. .-.. -..')
print('hello world')
print('>>> English: hello world')
print('.... . .-.. .-.. ---     .-- --- .-. .-.. -..')
print("Use 'quit()' to quit")

Morse_English = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-..':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '   ':' ', '':'', '--..--':',', '.-.-.-':'.', '..--..':'?', '---...':':', '.-..-.':'"', '-.-.--':'!'}

English_Morse = dict(zip(list(Morse_English.values()), list(Morse_English.keys())))

def Morse(x):
    for a in x:
        if a != '-' and a != '.' and a != ' ':
            return "Input must be Morse Code"
    x += ' '
    sentence = ''
    letter = ''
    i=0
    for a in x:
        if (a != ' '):
            i = 0
            letter += a
        else:
            i += 1
            if i == 3:
                sentence += ' '
                i=0
            else:
                if letter not in Morse_English:
                    return '"' + letter + '"' + " is not translatable"
                sentence += Morse_English[letter]
                letter = ''
    return sentence

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
    elif x == 'quit()':
        exit()
    else:
        try:
            eval(x)
        except Exception as e:
            print('Error: ' + str(e))