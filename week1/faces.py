def main() :
    text = input("Please enter string")
    formattedText = replaceText(text)
    print(formattedText)

def replaceText(str) :
    text = str.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()