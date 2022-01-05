
import turtle

max_length = 250
increment = 10


def draw_spiral(a_turtle, line_length):
    """
    recursive call example:
    run the turtle in a spiral until the max line length is reached

    :param a_turtle: turtle object "charlie"
    :type a_turtle: object
    :param line_length: length of line to draw
    :type line_length: int
    :return: recursive function call
    :rtype: func
    """

    # compare line_length to base-case (max_length)
    if line_length > max_length:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)

    # recursive call
    return draw_spiral(a_turtle, line_length + increment)


def main():
    charlie = turtle.Turtle(shape="turtle")
    charlie.pensize(5)
    charlie.color("red")
    draw_spiral(charlie, 10)
    turtle.done()


if __name__ == "__main__":
    main()

