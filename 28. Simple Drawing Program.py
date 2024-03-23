import turtle

def main():
    turtle.speed(0)
    turtle.shape("turtle")

    def draw_square():
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)

    for _ in range(100):
        draw_square()
        turtle.right(10)

    turtle.done()

if __name__ == "__main__":
    main()
