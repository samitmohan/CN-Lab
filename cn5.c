#include <stdio.h>
#include <string.h>

// Bit

int main() {
    int i, j, count = 0, nl;
    char str[100];

    printf("Enter the bit string: ");
    gets(str);

    for (i = 0; i < strlen(str); i++) {
        count = 0;
        for (j = i; j <= (i + 5); j++) {
            if (str[j] == '1') {
                count++;
            }
        }
        if (count == 6) {
            nl = strlen(str) + 2;
            for (; nl >= (i + 5); nl--) {
                str[nl] = str[nl - 1];
            }
            str[i + 5] = '0';
            i = i + 7;
        }
    }

    printf("The stuffed bit string: %s\n", str);
    return 0;
}

// Character
#include<stdio.h>
#include<string.h>

void char_stuffing(void);

int main() {
    int choice;

    while (1) {
        printf("\n\n\n1. Character stuffing");
        printf("\n2. Exit");
        printf("\nEnter choice: ");
        scanf("%d", &choice);

        if (choice > 2) {
            printf("\nInvalid option. Please re-enter.\n");
            continue;
        }

        switch (choice) {
            case 1:
                char_stuffing();
                break;
            case 2:
                return 0;
        }
    }
}

void char_stuffing(void) {
    char c[50], d[100], t[50];
    int i, m, j;

    printf("Enter the number of characters: ");
    scanf("%d", &m);

    printf("\nEnter the characters: ");
    getchar(); 
    for (i = 0; i < m; i++) {
        scanf("%c", &c[i]);
    }

    printf("\nOriginal data:\n");
    for (i = 0; i < m; i++) {
        printf("%c", c[i]);
    }

    d[0] = 'd';
    d[1] = 'l';
    d[2] = 'e';
    d[3] = 's';
    d[4] = 't';
    d[5] = 'x';

    for (i = 0, j = 6; i < m; i++, j++) {
        if ((c[i] == 'd' && c[i + 1] == 'l' && c[i + 2] == 'e')) {
            d[j] = 'd';
            j++;
            d[j] = 'l';
            j++;
            d[j] = 'e';
            j++;
            m = m + 3;
        }
        d[j] = c[i];
    }

    m = m + 6;
    m++;
    d[m] = 'd';
    m++;
    d[m] = 'l';
    m++;
    d[m] = 'e';
    m++;
    d[m] = 'e';
    m++;
    d[m] = 't';
    m++;
    d[m] = 'x';
    m++;

    printf("\nTransmitted data:\n");
    for (i = 0; i < m; i++) {
        printf("%c", d[i]);
    }

    for (i = 6, j = 0; i < m - 6; i++, j++) {
        if (d[i] == 'd' && d[i + 1] == 'l' && d[i + 2] == 'e' && d[i + 3] == 'd' && d[i + 4] == 'l' && d[i + 5] == 'e') {
            i = i + 3;
        }
        t[j] = d[i];
    }

    printf("\nReceived data:\n");
    for (i = 0; i < j; i++) {
        printf("%c", t[i]);
    }
}
