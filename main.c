#include "ternary.h"
#include <stdio.h>

int valve(int A, int B) {

	int block_a = AND(ON(A), ON(B));
	int block_b = SWITCH(AND(ON(A), ON(SWITCH(B))));
	int block_c = OR(block_a, block_b);

	return block_c;

}

int half_add(int A, int B) {

	int block_a = OR(OFF(A), OFF(B));
	int block_b = OR(A, B);
	int block_c = valve(block_a, block_b);
	int block_d = SWITCH(AND(A, B));
	int block_e = valve(OFF(block_a), block_d);
	int block_f = OR(block_c, block_e);

	return block_f;

}

void draw_truth_table(int (*f)(int, int)) {

	int a = 0;
	int b = 0;
	printf("A | B | X\n");
	printf("----------\n");

	for ( int i = 0; i < 9; i++ ) {
		
		if (b > 2) { b = 0; a++; }
		printf("%d | %d | %d\n", a, b, f(a, b));
		b++;
	
	}

}

void main() {
	
	int (*valve_function)(int, int) = &valve;
	int (*half_add_function)(int, int) = &half_add;
	draw_truth_table(half_add_function);

}















