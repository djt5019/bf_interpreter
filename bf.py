code = '''
+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set the next four cells to 70/100/30/10
    > +++++ ++              add  7 to cell #1
    > +++++ +++++           add 10 to cell #2
    > +++                   add  3 to cell #3
    > +                     add  1 to cell #4
    <<<< -                  decrement counter (cell #0)
]
> ++ .                  print 'H'
> + .                   print 'e'
+++++ ++ .              print 'l'
.                       print 'l'
+++ .                   print 'o'
> ++ .                  print ' '
<< +++++ +++++ +++++ .  print 'W'
> .                     print 'o'
+++ .                   print 'r'
----- - .               print 'l'
----- --- .             print 'd'
> + .                   print '!'
> .                     print '\n'
'''


valid_tokens = set('+-[]<>.,')


def parse_code(code):
    code = ''.join(ch for ch in code if ch in valid_tokens)

    balanced_brackets = (code.count('[') - code.count(']')) == 0

    if not balanced_brackets:
        raise SyntaxError('Unbalanced square brackets')

    return code


def evaluate(code, num_registers=10):
    registers = [0] * num_registers
    program_length = len(code)
    program_counter = 0
    register_index = 0

    loop_stack = []  # Keeps track of the loops starting point

    while program_counter < program_length:
        token = code[program_counter]

        if token == '>':
            register_index = min(register_index + 1, num_registers)

        elif token == '<':
            register_index = max(register_index - 1, 0)

        elif token == '+':
            registers[register_index] = min(registers[register_index] + 1, 255)

        elif token == '-':
            registers[register_index] = max(registers[register_index] + 1, 0)

        elif token == '[':
            # Save the location of the start of the loop
            if registers[register_index] != 0:
                loop_stack.append(program_counter + 1)
            else:
                program_counter = code[:program_counter].index(']')

        elif token == ']':
            if registers[register_index] != 0:
                program_counter = loop_stack.pop()

        elif token == '.':
            print chr(registers[register_index])

        elif token == ',':
            registers[register_index] = int(raw_input().strip())

        program_counter += 1


if __name__ == '__main__':
    clean_code = parse_code(code)
    evaluate(clean_code)
