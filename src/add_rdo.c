#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

    if(argc < 3){
        fprintf(stderr, "Usage: add_rdo <input> <output>\n");
        exit(1);
    }

    FILE *input, *output;
    char buffer[500];

    input = fopen(argv[1], "r");
    if(!input){
        fprintf(stderr, "%s doesn't exist!\n", argv[1]);
        exit(1);
    }

    output = fopen(argv[2], "w");
    if(!output){
        fprintf(stderr, "Open %s error!\n", argv[2]);
        exit(1);
    }

    char check[2];

    while(fgets(buffer, 100, input)){
        int last = strlen(buffer);
        buffer[last] = 0;
        fprintf(output, "%s %d\n", buffer, rand()%4);
		fgets(buffer, 100, input);
    }

    fclose(input);
    fclose(output);

	fprintf(stderr, "Success\n");
	return(0);

}
