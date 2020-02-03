def is_in_file(filename, string):
    """
    If string is in file?
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    # THE SAME:
    # f = open('test_file.txt', 'r')
    # lines = f.readlines()
    # f.close()

    for n, line in enumerate(lines):
        if string in line:
            return n, line

    return False


if __name__ == '__main__':
    res = is_in_file('test_file.txt', 'Agata')
    if res:
        print('Agata is in file:')
        print(*res)
    else:
        print('no Agata here...')

