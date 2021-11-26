from rich import pretty
from rich.console import Console

from EcuacionesLineales.gausspar import gausspar_menu
from EcuacionesLineales.gausstot import gausstot_menu
from EcuacionesLineales.gausspl import gausspl_menu
from EcuacionesLineales.gseidel import gseidel_menu
from EcuacionesLineales.jacobi import jacobi_menu
from EcuacionesLineales.LUsimple import LUsimple_menu

from Interpolacion.vandermonde import vandermonde_menu
from Interpolacion.difDividas import difdivid_menu


pretty.install()
console = Console()


def display_menu(options):
    console.print('Seleccione una opción con un número', style='bold green on black')
    keys = list(options.keys())
    for i, option in enumerate(keys):
        console.print(f'[bold cyan]{i + 1})[/bold cyan] {option}')
    seleccion = int(input('\n> ')) - 1
    if 0 <= seleccion < len(keys):
        new_options = options[keys[seleccion]]
        return new_options
    else:
        console.print('Opción incorrecta', style='bold red on black')


single_var = {}
lineal = {'Gauss par': gausspar_menu, 'Gauss simple': gausspl_menu, 'Gauss seidel': gseidel_menu, 'Gauss total': gausstot_menu, 'Jacobi': jacobi_menu, 'LU simple': LUsimple_menu}
interpolation = {'Vandermonde': vandermonde_menu, 'Diferencias divididas': difdivid_menu}
categorias = {'Ecuaciones de una variable': single_var, 'Ecuaciones lineales': lineal, 'Interpolación': interpolation}


# [[-7 2 -3 4], [5 -1 14 -1], [1 9 -7 5], [-12 13 -8 -4]]

seleccion = display_menu(categorias)
seleccion = display_menu(seleccion)
seleccion()
