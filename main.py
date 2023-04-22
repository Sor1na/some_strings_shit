def main():
    a = input()

    alphabet = open('morse_alpha.txt', 'r')
    list1 = alphabet.readlines()
    for element in range(len(list1)):
        list1[element] = list1[element].split()
    translated_line = ''
    
    for letter in a:
        for element in range(len(list1)):
            if letter.upper() ==  list1[element][0]:
                translated_line = translated_line + list1[element][1]
        if letter == ' ':
            translated_line = translated_line + '/'
        
    print(translated_line)
    
if __name__ == '__main__':
    main()
