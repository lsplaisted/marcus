import menu

import program1, program2

programs = {
    0: program1.Run,
    1: program2.Run,
}

menu.menu(programs)
