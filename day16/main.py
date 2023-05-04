# from turtle import Turtle, Screen  # Turtle ở đây là một class
# quoc_vuong = Turtle()
# quoc_vuong.color('red')
# quoc_vuong.shape('triangle')
# quoc_vuong.forward(100)
# quoc_vuong.left(5000)
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
table.align = 'c'
print(table)
