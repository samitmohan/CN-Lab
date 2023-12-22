# CRC is used to check error in a transmitted message.

"""
Steps -:
1) Take input : input polynomial, gp
2) Add len(gp) bits to input (0 bits) : divisor
XOR
3) Go through every bit in input : Check if divisor AND gp have 1 or 0 bits at same place : Result = 0 else 1
4) Join divisor answer and return.
"""


def crc(inp, gp, mode): # mode is for converting
    divisor = list(inp)
    if mode:
        divisor += ['0'] * (len(gp) - 1) # 2
    for i in range(len(inp)): # 3 
        if divisor[i] == '1': # it is divisible : check for XOR condition
            for j in range(len(gp)):
                if (divisor[i + j] == '0' and gp[j] == '0') or (divisor[i + j] == '1' and gp[j] == '1'):
                    divisor[i + j] = '0' # xor op 0 if same
                else:
                    divisor[i + j] = '1'
    return ''.join(divisor) # 4


def main():
    inp = input("Enter inp in binary : ")
    gp = input("Enter GP : ")
    ans = crc(inp, gp, True) # calc xor
    print(f"The transmitted message is {inp} {ans[len(inp):]}") # remember ans[len(inp) : ]
    # check if recieved bits remainder = 0 :: no error 
    recieved = input("Enter recieved message in binary : ")
    if crc(recieved, gp, False).endswith('0'):
        print("No error")
    else:
        print("Error")
main()