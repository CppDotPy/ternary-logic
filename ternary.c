
int validate(int number) {

	if ( number > 2 || number < 0 ) { return 0; }
	else { return 1; }

}

int ternary(char A) {

	int output;
	switch(A) {
		case 0: return 0;
		case 1: return 2;
		case 2: return 3;
	}

}

int AND(int A, int B) {
	if ( validate(A) == 0 ) { return -1; }
	if ( validate(B) == 0 ) { return -1; }

	if ( A == B ) { return A; }
	else { return 0; }

}

int OR(int A, int B) {
	if ( validate(A) == 0 ) { return -1; }
	if ( validate(B) == 0 ) { return -1; }

	return ((A) >= (B)) ? (A) : (B);

}

int ON(int A) {
	if ( validate(A) == 0 ) { return -1; }

	if ( A == 2 ) { return 2; }
	else { return 0; }

}

int OFF(int A) {
	if ( validate(A) == 0 ) { return -1; }

	if ( A == 0 ) { return 2; }
	else { return 0; }

}

int SWITCH(int A) {
	if ( validate(A) == 0 ) { return -1; }

	switch(A) {
		case 0: return 0;
		case 1: return 2;
		case 2: return 1;
	}

}

