import sqlite3

# Variables globales       
db = sqlite3.connect('stock.sqlite')
cursor = db.cursor()
op_final = 's'
nombre_usuario = 'alessi'
        
def main():
    op = 'a'
    menu = '\n(1) Reiniciar tabla productos'\
           '\n(2) Insertar producto'\
           '\n(3) Mostrar productos'\
           '\n(4) Mostrar producto especifico'\
           f'\n({op_final}) Para salir: '
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
          f'\nBuen dia {nombre_usuario} ¿que queres hacer?'
          '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


    while op != op_final:
        op = input(menu)
        
        if op == '1':
            cursor.execute('DROP TABLE IF EXISTS productos')
            cursor.execute('CREATE TABLE productos (nombre TEXT, cantidad INTEGER, precio INTEGER)')
            db.close()            

        elif op == '2':
            cursor.execute('INSERT INTO productos (nombre, cantidad, precio) VALUES (?,?,?)', ('queso', 2, 2500))
            db.commit()
                
        elif op == '3':
            print('Productos:')
            cursor.execute('SELECT nombre, cantidad, precio FROM productos')
            for fila in cursor:
                print(' '.join(map(str, fila)))
               
        elif op == '4':
            cursor.execute('SELECT precio FROM productos WHERE nombre = "queso"')
            for fila in cursor:
                print(fila[0])

        elif op == op_final:
            print('\n' + '=' * 16)
            print('Hasta luego')
            print('=' * 16)
        else:
            error('Error. Ingresa un valor valido')
               
if __name__ == '__main__':
    main()
