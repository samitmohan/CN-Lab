# bti stuff

def bs(inp):
    i = 0
    while i < len(inp):
        if inp[i:i+6] == '111111':
            inp = inp[i:i+5] + '0' + inp[i+5:]
            i += 7
        else:
            i += 1
    return inp

def cs():
    og_data = input("Enter characters : ")
    print("Original Data : ", og_data)
    t_data = "dlestx"
    i, j = 0, 6
    for i in range(len(og_data)):
        if og_data[i:i+3] == 'dle':
            t_data += 'dle'
            i += 3
        t_data += og_data[i]
    og_len = len(t_data)
    og_len += 6
    t_data += 'dleetx'
    print("Transmitted data : ", t_data)

    r_data = ""
    i = 6
    while i < og_len - 6:
        if t_data[i:i+6] == 'dledle':
            i += 3
        r_data += t_data[i]
        i += 1
    print("Recieved data : ", r_data)


def main():
    # inp = input("Enter message to be transferred in bits : ")
    # print(f"Stuffed message : {bs(inp)}")
    choice = int(input("Enter choice : "))
    if choice:
        cs()
    else:
        return 0
main()