def crc(inp, gp, mode):
    div = list(inp)
    if mode: 
        div += ['0'] * (len(gp)-1)
    for i in range(len(inp)):
        if div[i] == '1':
            for j in range(len(gp)):
                if (div[i+j] == '1' and gp[j] == '1') or (div[i+j] == '0' and gp[j] == '0'):
                    div[i+j] = '1'
                else: 
                    div[i+j] = '0'
    return ''.join(div)
def main():
    inp = input("Enter inp in binary : ")
    gp = input("Enter GP : ")
    ans = crc(inp, gp, True)
    print(f"Transmitted message {ans} {ans[len(inp):]}")
    rec = input("Enter recieved in binary : ")
    if crc(rec, gp, False).endswith('0'): print("No error")
    else:
        print("error")
main()