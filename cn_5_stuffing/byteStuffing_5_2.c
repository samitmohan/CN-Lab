#include<stdio.h>
#include<string.h>

void char_stuffing(void) {
    char og_data[50], t_data[100], recieve_data[50];
    int i, og_length, j;

    // Taking input of number of characters, characters and printing OG data
    printf("Enter the number of characters: ");
    scanf("%d", &og_length);

    printf("Enter the characters: ");
    getchar(); 
    for (i = 0; i < og_length; i++) {
        scanf("%c", &og_data[i]);
    }

    printf("Original data:\n");
    for (i = 0; i < og_length; i++) {
        printf("%c", og_data[i]);
    }

    // Copy dlestx (delmitter) into transmitted data
    strcpy(t_data, "dlestx");

    // go through first 6 characters (2 pointers i (0) and j (6)) and if dle present consec then add it to transmitted data and j++
    for (i = 0, j = 6; i < og_length; i++, j++) {
        if ((og_data[i] == 'd' && og_data[i + 1] == 'l' && og_data[i + 2] == 'e')) {
            t_data[j++] = 'd';
            t_data[j++] = 'l';
            t_data[j++] = 'e';
            og_length += 3; // already gone through first 3 (dle) characters
        }
        t_data[j] = og_data[i]; // update transmitted data pointer
    }

    og_length += 6; // dle-etx done
    t_data[og_length++] = 'd';
    t_data[og_length++] = 'l';
    t_data[og_length++] = 'e';
    t_data[og_length++] = 'e';
    t_data[og_length++] = 't';
    t_data[og_length++] = 'x';

    printf("\nTransmitted data:\n");
    for (i = 0; i < og_length; i++) {
        printf("%c", t_data[i]);
    }

    // Convert transmitted -> recieved if dledle found then i+=3
    for (i = 6, j = 0; i < og_length - 6; i++, j++) {
        if (t_data[i] == 'd' && t_data[i + 1] == 'l' && t_data[i + 2] == 'e' && t_data[i + 3] == 'd' && t_data[i + 4] == 'l' && t_data[i + 5] == 'e') {
            i = i + 3;
        }
        recieve_data[j] = t_data[i];
    }

    printf("\nReceived data:\n");
    for (i = 0; i < j; i++) {
        printf("%c", recieve_data[i]);
    }
}

int main() {
    int choice;
    while (1) {
        printf("\n 1. Character stuffing");
        printf("\n 2. Exit");
        printf("Enter choice: ");
        scanf("%d", &choice);
        if (choice > 2) {
            printf("\nInvalid option. Please re-enter.\n");
            continue;
        }
        switch (choice) {
            case 1:
                char_stuffing(); break;
            case 2: return 0;
        }
    }
}