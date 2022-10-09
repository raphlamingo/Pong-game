balls.move()
    screen.update()
    if balls.ycor()>250 or balls.ycor()<-250:
        balls.change()
    if balls.distance(paddy.paddle)<50 and balls.xcor()>690:
        balls.bounce()

    game = False


