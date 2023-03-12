#create main function
def main():
    text = input()
    print(convert(text))

#create convert function
def convert(str):
    txt1 = str.replace(":)", "🙂")
    txt2 = txt1.replace(":(", "🙁")
    return txt2
#call main function
main()
