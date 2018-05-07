from __future__ import print_function
from collections import namedtuple

X, O = 'X', None
Tetromino = namedtuple("Tetrimino", "color shape")

list_of_tetrominoes = [
    Tetromino(color=(47, 64, 224),
              shape=((O,O,X,O,O),
                     (O,O,X,O,O),
                     (O,O,X,O,O),
                     (O,O,X,O,O),
                     (O,O,X,O,O))),
    Tetromino(color=(124, 252, 0),
              shape=((O,O,X,O),
                     (O,X,X,O),
                     (O,O,X,O),
                     (O,O,X,O))),
    Tetromino(color=(225, 242, 41),
              shape=((O,O,X,O),
                     (O,O,X,O),
                     (O,X,X,O),
                     (O,X,O,O))),
    Tetromino(color=(22, 181, 64),
              shape=((O,O,X,O),
                     (O,O,X,O),
                     (O,O,X,O),
                     (O,X,X,O))),
    Tetromino(color=(10, 255, 226),
              shape=((O,X,X),
                     (O,X,O),
                     (X,X,O))),
    Tetromino(color=(244, 164, 96),
              shape=((X,X,O),
                     (X,X,O),
                     (O,X,O))),
    Tetromino(color=(204, 22, 22),
              shape=((O,X,O),
                     (X,X,X),
                     (O,X,O))),
    Tetromino(color=(242, 41, 195),
              shape=((O,O,X),
                     (O,X,X),
                     (X,X,O))),
    Tetromino(color=(255, 248, 220),
              shape=((O,O,X),
                     (O,O,X),
                     (X,X,X))),
    Tetromino(color=(95, 158, 160),
              shape=((O,O,O),
                     (X,O,X),
                     (X,X,X))),
    Tetromino(color=(245, 144, 12),
              shape=((O,X,X),
                     (X,X,O),
                     (O,X,O))),
    Tetromino(color=(85, 107, 47),
              shape=((X,X,X),
                     (O,X,O),
                     (O,X,O))),
    ]

def rotate(shape, times=1):
    """ Rotate a shape to the right """
    return shape if times == 0 else rotate(tuple(zip(*shape[::-1])), times-1)


def shape_str(shape):
    """ Return a string of a shape in human readable form """
    return '\n'.join(''.join(map({'X': 'X', None: 'O'}.get, line))
                     for line in shape)

def shape(shape):
    """ Print a shape in human readable form """
    print(shape_str(shape))





def test():
    tetromino_shapes = [t.shape for t in list_of_tetrominoes]
    map(rotate,    tetromino_shapes)
    map(shape,     tetromino_shapes)
    map(shape_str, tetromino_shapes)

    assert shape_str(T_left_snake.shape) == "XXO\nOXX\nOOO"

    assert rotate(T_square.shape) == T_square.shape

    assert rotate(T_right_snake.shape, 4) == T_right_snake.shape

    assert rotate(T_hat.shape)    == ((O,X,O),
                                      (O,X,X),
                                      (O,X,O))

    assert rotate(T_hat.shape, 2) == ((O,O,O),
                                      (X,X,X),
                                      (O,X,O))
    print("All tests passed in {}, things seems to be working alright".format(__file__))

if __name__ == '__main__':
    test()
