def break_pieces(shape):
    shape = shape.split('\n')

    return shape


if __name__ == "__main__":
    shape = '\n'.join(["+------------+",
                       "|            |",
                       "|            |",
                       "|            |",
                       "+------+-----+",
                       "|      |     |",
                       "|      |     |",
                       "+------+-----+"])

    solution = break_pieces(shape)
    print(solution)
