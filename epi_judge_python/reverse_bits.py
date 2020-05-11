from test_framework import generic_test

class BitReverser:
    def __init__(self):
        pass

    def sixty_four_bit_reverse(self, val):
        constructed_val = 0
        if self._is_odd(val):
            constructed_val = constructed_val + 1

        for i in range(0,63):
            val = val >> 1
            constructed_val = constructed_val << 1
            if self._is_odd(val):
                constructed_val = constructed_val + 1

        return constructed_val

    def _is_odd(self, val):
        return val % 2 == 1

def reverse_bits(x: int) -> int:
    reverser = BitReverser()
    return reverser.sixty_four_bit_reverse(x)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
