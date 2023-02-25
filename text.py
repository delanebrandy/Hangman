from hangman_img import number_wrong

app = App(title = 'Quiz Time', height = 300, width = 500)
picture = Picture(app, image=number_wrong[2])
app.display()