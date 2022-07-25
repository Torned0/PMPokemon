def checkinput(buffer: str) -> int:
    buffer = buffer.upper()
    for letter in buffer:
        if letter == 'E' or letter == 'O' or letter == 'N' or letter == 'S':
            continue
        else:
            if buffer == 'QUIT':
                return -1
            return 1
    return 0


def move(path: str) -> int:
    x, y = 0, 0
    positions = {(x, y)}
    for step in path:
        match step:
            case 'N':
                x, y = x, y + 1
            case 'S':
                x, y = x, y - 1
            case 'E':
                x, y = x + 1, y
            case 'O':
                x, y = x - 1, y
        positions.add((x, y))
    return len(positions)


def prompt():
    while True:
        buffer = input("Qual o caminho que o Ash vai percorrer?\n")
        flag = checkinput(buffer)
        if flag == -1:
            print("A terminar o programa\n")
            exit(0)
        if flag == 1:
            print("Caminho inválido")
        if flag == 0:
            count = move(buffer.upper())
            print("O Ash apanhou {0} pokemons".format(count))


if __name__ == '__main__':
    prompt()
