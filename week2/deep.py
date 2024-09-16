
def checkAnswer(answer):
    if answer == "42" or answer == "forty-two":
        return True
    return (answer == "forty two")

def main():
    answer = input("what is the answer to the Great Question of Life, the Universe and Everything?")
    if checkAnswer(answer):
        print("Yes")
    else:
        print("No")

main()
        