#include <stdio.h>

int a = 1, b = 108400, c = 125400, d = 0, e = 0, f = 0, g = 0, h = 0;

int main(void) {
    do {
        f = 1;
        d = 2;
        do {
            if(b%d == 0){
                f = 0;
            }
            d = d + 1;
            g = d;
            g = g -b;
        } while(g != 0);
        if(f == 0){
            h = h + 1;
        }
        g = b;
        g = g - c;
        if (g == 0){
            printf("h: %d\n", h);
            return 0;
        }
        b = b +17;
    } while(1);
}
