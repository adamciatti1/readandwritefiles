def main():

    #Open a file named philosphers.txt
    infile = open('philosphers.txt', 'r')

    #Read the file's contents
    ###file_contents = infile.read() OR
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    #Print the data
    ###print(file_contents) OR
    print(line1)
    print(line2)
    print(line3)

    #Close the file
    infile.close()


main()
