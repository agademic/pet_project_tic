
PROGRAM = '>>>>>p+p>++p>+++p<<<<+++p>p+p+++++>+p<<-p'

memory = [0 for i in range(10)]
index = 0
for cmd in PROGRAM:
    if cmd == '+':
        memory[index] += 1
    elif cmd == '-':
        memory[index] -= 1
    if cmd == '>':
        index += 1
    elif cmd == '>':
        index -= 1
    elif cmd == 'p':
        print(memory[index])
