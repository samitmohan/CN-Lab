def stopWait():
    frames = int(input("Enter the number of frames: "))
    sent = 0
    while True:
        for i in range(frames):
            print(f"Frame {sent} has to be transmitted")
            sent += 1
            if sent == frames: break

        ack = int(input("Last ack recieved : "))
        if ack >= frames: break
        sent = ack # else

def main():
    stopWait()
main()