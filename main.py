def count_digits(line):
    digit = (len([i for i in line if i.isdigit()]))
    alphabet = (len([i for i in line if i.isalpha()]))
    return digit

def main():
    line = input()
    print (count_digits(line))



if __name__ == '__main__':
    main()