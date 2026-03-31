from marcus.menu import menu

import program1, program2

programs = [
    program1.Run,
    program2.Run,
]

menu(programs)

print("done")