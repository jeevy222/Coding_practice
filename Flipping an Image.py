'''Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].'''


def flip_and_invert_image(matrix):
    # TODO: Write your code here.
    matrix_flipped = []
    for i in matrix:
        j = i[::-1]
        q = []
        for k in range(len(j)):
            l = j[k] ^ 1
            q.append(l)
        matrix_flipped.append(q)

    return matrix_flipped


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()


'''def flip_an_invert_image(matrix):
    C = len(matrix)
    for row in matrix:
        for i in range((C + 1) // 2):
            row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1  (~i = C-i-1)

    return matrix


def main():
    print(flip_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_an_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()'''