import argparse

def main():
    #1. Le asignamos el valor de la funcion parse_args a la variable args
    args = parse_args ()

    args.func (args)

def parse_args ():
    #2. Creamos el objeto que se encargará de leer la terminal
    parser = argparse.ArgumentParser ()

    #3. Creamos la variable commands, que servira como estructura para permitir los comandos en CLI
    commands = parser.add_subparsers (dest='command')#3.1 El contenido de la instruccion ira a la variable command
    commands.required = True #3.2 Aqui hacemos que sea obligatorio poner un comando

    #4. Creamos el objeto init
    init_parser = commands.add_parser ('init')
    #4.1 Por predeterminado le asignamos la funcion init
    init_parser.set_defaults (func=init)

    return parser.parse_args ()

def init (args):
    print ('Hola, esto es migit')