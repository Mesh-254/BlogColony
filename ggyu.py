import turtle

#function to draw a square with side length
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# function to draw hpnotic pattern
def draw_hypnotic_pattern(num_squares, initial_side_length, side_length_increment):
    for _ in range(num_squares):
        draw_square(initial_side_length)
        turtle.right(360 / num_squares)
        initial_side_length += side_length_increment

#main function
def main():
    turtle.speed(2)

    num_squares = int(input("Enter the number of squares: "))
    initial_side_length = int(input("Enter the initial side length: "))
    side_length_increment = int(input("Enter the side length increment: "))

    draw_hypnotic_pattern(num_squares, initial_side_length, side_length_increment)

    turtle.done()

if __name__ == "__main__":
    main()