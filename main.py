from ternary_logic import ternary, math

def valve(A, B):

	block_a = A.on() + B.on()
	block_b = (A.on() + B.switch().on()).switch()
	output = block_a ^ block_b
	return output

def half_add(A, B):

	block_a = A.off() ^ B.off()
	block_b = A ^ B
	block_c = valve(block_a, block_b)
	block_d = (A + B).switch()
	block_e = valve(block_a.off(), block_d)
	output = block_c ^ block_e
	return output


def draw_truth_table(function):

	print()
	print('A | B | X')

	a = ternary(ternary.G)
	b = ternary(ternary.G)

	for i in range(9):

		if b.state == ternary.G: a.count()
		b.count()
		print('__________')
		print(f'{a} | {b} | {function(a, b)}')
	print()

def main():

	r = ternary(ternary.R)
	b = ternary(ternary.B)
	g = ternary(ternary.G)

	draw_truth_table(valve)

if __name__ == '__main__': main()
