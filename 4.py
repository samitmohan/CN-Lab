def lb():
    bucket_lvl, drop = 0,0
    cap = int(input("Enter capacity : "))
    process = int(input("Enter process rate : "))
    sec = int(input("Enter seconds : "))
    packet_size = []
    for i in range(sec):
        size = int(input(f"Enter size for {i+1} packet : "))
        packet_size.append(size)
    print("\n Seconds | Packet Recieved | Packet Sent | Packet Left | Packet Dropped")

    for i in range(sec):
        bucket_lvl += packet_size[i]
        if bucket_lvl > cap:
            drop = bucket_lvl - cap
            bucket_lvl = cap
        packet_sent = min(bucket_lvl, process)
        bucket_lvl -= packet_sent
        print(f"{i+1} \t {packet_size[i]} \t\t {packet_sent} \t\t {bucket_lvl} \t\t {drop}")
        drop = 0

    while bucket_lvl:
        if bucket_lvl > cap:
            drop = bucket_lvl - cap
            bucket_lvl = cap
        packet_sent = min(bucket_lvl, process)
        bucket_lvl -= packet_sent
        print(f"{i+1} \t 0 \t\t {packet_sent} \t\t {bucket_lvl} \t\t {drop}")
        i += 1
        drop = 0

if __name__ == "__main__":
    lb()