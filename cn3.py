def stopWait():
    fs = int(input("Enter the number of frames: "))
    sent = 0
    while True:
        for i in range(fs):
            print(f"Frame {sent} has to be transmitted")
            sent += 1
            if sent == fs: break

        ack = int(input("Please enter the last acknowledgment received: "))
        if ack >= fs: break
        else:
            sent = ack

def main():
    stopWait()
main()