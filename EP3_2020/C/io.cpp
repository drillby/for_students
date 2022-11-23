#include <stdio.h>
#include <string.h>

int main() {
	/*
	int cele_cislo;
	scanf("%d", &cele_cislo);
	printf("Cele cislo: %d", cele_cislo);
	*/
	/*
	float desetinne_cislo; // mùže být i double
	printf("Zadej èíslo: ");
	scanf("%f", &desetinne_cislo);
	printf("Desetinne cislo: %.1f", desetinne_cislo);
	*/
	
	/*
	char znak;
	printf("Zadej znak: ");
	scanf("%c", &znak);
	printf("znak: %c", znak);
	*/
	
	// declare and initialize string
    char str[10];
    scanf("%s", &str);
  
    // print string
    printf("%s\n", str);
    
    int length = 0;
    length = strlen(str);
    
    // displaying the length of string
    printf("Length of string str is %d", length);

	
	return 0;
}
