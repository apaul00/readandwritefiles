def main():

    outfile = open("philosophers.txt", "w")

    outfile.write("John Locke" + "\n")
    outfile.write("David Hume" + "\n")
    outfile.write("Edmund Burke" + "\n")

    outfile.close()


def addMyName():
    outfile = open("philosophers.txt", "a")

    outfile.write("Andrew Scalia" + "\n")

    outfile.close()


main()
addMyName()  # calls
