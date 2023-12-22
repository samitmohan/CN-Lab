# Bit Stuffing
def stuffed(inp):
    i = 0
    while i < len(inp):
        # if anywhere in inp you see 6 consec 1s : add 0 bit stuff and slide the window by 7 bits (next)
        if inp[i: i + 6] == '111111':
            inp = inp[:i+5] + '0' + inp[i+5:] # add 0 between 5th and 6th bit
            i += 7
        else:
            i += 1 # shift window to next to see
    return inp

def main():
    inp = input("Enter message : ")
    print("Bit stuffed message : ", stuffed(inp))
main()