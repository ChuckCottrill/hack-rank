// https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#include <stdio.h>
#include <math.h>

#define SIZE 100000

int K[SIZE];

long
isKaprekar(int x)
{
    long int sum;
    long int a = 0;
    long int k = i;
    while(k>0) {
        k/=10;
        ++a;
    }
    long int p = x * x;
    long int g = pow(10,a);
    sum = p%g + p/g;
    return sum == x;
}

void
kaprekar() {
    long i, j, n, sq, dNo, mid, left, right, d[12];
   
    for(n = 1; n < SIZE; n++) {
        sq = n * n;
        
        dNo = 0;
        while(sq) {
            d[++dNo] = sq % 10;
            sq /= 10;
        }
        
        mid = dNo / 2;
        for(j = dNo, i = 1; i <= dNo/2; i++, j--) d[i] ^= d[j] ^= d[i] ^= d[j];
        
        for(left = j = 0, i = mid; i >= 1; i--, j++) {
            left += d[i] * pow(10, j);
        }
        for(right = j = 0, i = dNo; i >= mid + 1; i--, j++) {
            right += d[i] * pow(10, j);
        }

        if(left + right == n) K[n] = 1;
        else                  K[n] = 0;
    }
}

int main() {
    long int p,q; // r,f;
    int count = 0;
    scanf("%ld\n%ld",&p,&q);
    for( long int x=p; x<=q; x++ ) {
        if (isKaprekar(x)) {
            printf("%ld ",x);
            count++;
        }
    }
    if(count == 0)
        printf("INVALID RANGE");       
    return 0;
}


int main() {
   
    kaprekar();
    
    int i, p, q, flag;
    scanf(" %d %d", &p, &q);
    
    for(flag = 1, i = p; i <= q; i++) {
        if(K[i]) {
            printf("%d ", i);
            flag = 0;
        }
    }
    if(flag) printf("INVALID RANGE");
    
    return 0;
}


