def sw():
    frames = int(input("Enter number of frames :"))
    sent = 0
    while True:
        for i in range(frames):
            print(f"Frame to be transmitted {sent}")
            sent += 1
            if sent == frames: break
        ack = int(input("Enter last ack recieved : "))
        if ack >= frames: break
        else:
            sent = ack

if __name__ == "__main__":
    sw()