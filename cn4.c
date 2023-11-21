#include <stdio.h>

int min(int x, int y) {
    return (x < y) ? x : y;
}

int main() {
    int drop = 0, mini, nsec, cap, count = 0, i, inp[25], process;

    printf("Enter The Bucket Size: ");
    scanf("%d", &cap);

    printf("Enter The Processing Rate: ");
    scanf("%d", &process);

    printf("Enter The No. Of Seconds You Want To Stimulate: ");
    scanf("%d", &nsec);

    for (i = 0; i < nsec; i++) {
        printf("Enter The Size Of The Packet Entering At %d sec: ", i + 1);
        scanf("%d", &inp[i]);
    }

    printf("\nSecond | Packet Received | Packet Sent | Packet Left | Packet Dropped |\n");
    printf("---------------------------------------------------------------------\n");

    for (i = 0; i < nsec; i++) {
        count += inp[i];

        if (count > cap) {
            drop = count - cap;
            count = cap;
        }

        printf("%d\t%d\t\t%d\t\t%d\t\t%d\n", i + 1, inp[i], (mini = min(count, process)), (count -= mini), drop);
        drop = 0;
    }

    for (; count != 0; i++) {
        if (count > cap) {
            drop = count - cap;
            count = cap;
        }

        printf("%d\t0\t\t\t%d\t\t%d\t\t%d\n", i + 1, (mini = min(count, process)), (count -= mini), drop);
    }

    return 0;
}
