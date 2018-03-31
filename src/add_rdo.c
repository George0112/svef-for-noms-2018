#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FRAME_SIZE 10000

int main(int argc, char **argv){

    if(argc < 4){
        fprintf(stderr, "Usage: add_rdo <encodeOutput> <input> <output>\n");
        exit(1);
    }

    FILE *encode ,*input, *output;
    char buffer[500];
	printf("%s\n", argv[1]);

	encode = fopen(argv[1], "r");
	if(!encode)
		fprintf(stderr, "%s doesn't exist!\n", argv[1]);

    input = fopen(argv[2], "r");
    if(!input){
        fprintf(stderr, "%s doesn't exist!\n", argv[2]);
        exit(1);
    }

    output = fopen(argv[3], "w");
    if(!output){
        fprintf(stderr, "Open %s error!\n", argv[3]);
        exit(1);
    }

    char check[2], par[20];

	int i, j, level, size[FRAME_SIZE];
	double Y[FRAME_SIZE], nouse, difference;

	for(i = 0; i < 3; i++)
		fgets(buffer, 100, encode);

	i = 0;

	while(fscanf(encode, "%s",par) != EOF){
		if(!strcmp(par, "Y")){
			fscanf(encode, "%lf", &Y[i]);
		}else if(!strcmp(par,"Level")){
			fscanf(encode, "%d", &level);
			printf(" level = %d\n", level);
		}else if(!strcmp(par, "V")){
			fscanf(encode, "%lf", &nouse);
			fscanf(encode, "%d", &size[i]);
			printf(" i = %d, Y[i] = %lf, Y[i-1] = %lf, PSNR Difference = %lf, ratio = %lf\n",
				 i, Y[i], i%4==0?0:Y[i-1], Y[i]-(((i%4)==0)?0:Y[i-1]), (Y[i]-(((i%4)==0)?0:Y[i-1]))/size[i]*1000000);
			i++;
		}
	}

	for(i = 0; i < 9; i++){
		fgets(buffer, 100, input);
		fgets(buffer, 100, input);
	}

	i = 0; j = 0;

    while(fgets(buffer, 100, input)){
		fprintf(output, "%s 0\n", buffer);
		fgets(buffer, 100, input);
		for(j = 0; j < 4; j++){
			fgets(buffer, 100, input);
			int last = strlen(buffer);
			buffer[last] = 0;
			fprintf(output, "%s %lf\n", buffer, (Y[i]-(((i%4)==0)?0:Y[i-1]))/size[i]*1000000);
			fgets(buffer, 100, input);
			i++;
		}
    }

    fclose(input);
    fclose(output);

	fprintf(stderr, "Success\n");
	return(0);

}
