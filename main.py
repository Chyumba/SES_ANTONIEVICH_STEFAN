def count_digits(line):
    digit = (len([i for i in line if i.isdigit()]))
    alphabet = (len([i for i in line if i.isalpha()]))
    return digit

# def test_digits():
#     assert count_digits ('абвгд123АБВГД') == 3

def main():
    line = input()
    print (count_digits(line))
    #test_digits()


if __name__ == '__main__':
    main()