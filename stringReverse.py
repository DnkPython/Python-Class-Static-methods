def strReverse(str1):
    new_string = []
    index = len(str1)
    while index:
        index -= 1
        new_string.append(str1[index])
    return ''.join(new_string)
if __name__=="__main__":
    a_str = "HELLO AADHYAA"
    print(strReverse(a_str))
