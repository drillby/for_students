#include <stdio.h>

// Pøedávání hodnotou
int secti(int a, int b)
{
    return a + b;
}

// Pøedávání hodnotou
void prohod(int a, int b)
{
    int pomocna = a;
    a = b;
    b = pomocna;
}


// Pøedávání referencí
void prohod_spravne(int *p_a, int *p_b)
{
    int pomocna = *p_a;
    *p_a = *p_b;
    *p_b = pomocna;
}

int main()
{
    int cislo1 = 15;
    int *adresa_cislo_1 = &cislo1;
    int cislo2 = 8;
    //int vysledek = secti(cislo1, cislo2);
    //printf("Vysledek je %d", vysledek);
   // printf("%d \n", &cislo1);
   // printf("%d", *adresa_cislo_1);

    prohod(cislo1, cislo2);
    printf("V cislo1 je èíslo %d a v cislo2 je èíslo %d. \n", cislo1, cislo2);
	
    prohod_spravne(&cislo1, &cislo2);
    printf("V a je èíslo %d a v b je èíslo %d.", cislo1, cislo2);
    
    return 0;
    // Co si zapamatovat?
    // pointer == promìnná ve které se nachází adresa do pamìti
    // & zjišuje adresu
    // * zjišujì hodnotu na adrese
}
