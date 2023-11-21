def crc(input_str, gp, mode):
    output_str = list(input_str)

    if mode:
        output_str += ['0'] * (len(gp) - 1)

    for j in range(len(input_str)):
        if output_str[j] == '1':
            for k in range(len(gp)):
                if (output_str[j + k] == '0' and gp[k] == '0') or (output_str[j + k] == '1' and gp[k] == '1'):
                    output_str[j + k] = '0'
                else:
                    output_str[j + k] = '1'

    return ''.join(output_str)


def main():
    input_str = input("\nEnter the input message in binary:\n")
    gp = input("\nEnter the generator polynomial:\n")

    transmitted_message = crc(input_str, gp, True)
    print(f"\nThe transmitted message is {input_str} {transmitted_message[len(input_str):]}")

    received_message = input("\nEnter the received message in binary:\n")

    if crc(received_message, gp, False).endswith('0'):
        print("\nNo error in data\n")
    else:
        print("\nError in data transmission has occurred\n")


if __name__ == "__main__":
    main()
