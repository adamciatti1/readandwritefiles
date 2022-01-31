def main():

    #Open a file named philosphers.txt
    outfile = open('philosphers.txt', 'w')

    #Write the names of three philosphers
    outfile.write('John Locke' + '\n')
    outfile.write('David Hume' + '\n')
    outfile.write('Edmund Burke' + '\n')

    #Close the file
    outfile.close()

def add_my_name():
    outfile = open('philosphers.txt', 'a')
   
    outfile.write('Adam Ciatti\n')
    
    oufile.close()

main()
add_my_name()