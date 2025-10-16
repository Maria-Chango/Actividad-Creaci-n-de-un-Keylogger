# Activity-Keylogger

Explanation of the Keylogger Script in Python
This script uses the keyboard library to monitor all keystrokes on the system and record them in a log file.

---------Prerequisites---------

To run this code, you must first install the keyboard library:

pip install keyboard

---------------Analysis:---------------------------------------

1. Importing the Library
import keyboard
This line imports the keyboard library, which provides cross-platform functionality for controlling and monitoring keyboard events.

2. Defining the Callback Function
def keyboard_event(event):
    with open(‘keylogger.log’,'a') as file:
        file.write(event.name)
   
def keyboard_event(event):  Defines the function that will be executed each time a key is pressed. 
The event parameter is an object provided by the keyboard library, which contains details about the keystroke.

with open(‘keylogger.log’,'a') as file: Opens a file called keylogger.log. The ‘a’ mode (append) ensures that each new keystroke is added to 
the end of the file without overwriting the previous content.

file.write(event.name): The event object has a property called name, which contains the name of the key that was pressed (e.g., ‘a’, ‘space’, ‘enter’, ‘shift’). 
This key name is written to the log file.

3. keyboard.on_press(keyboard_event)
This is the command that starts the monitoring process.
keyboard.on_press() registers the keyboard_event function as a callback function.
From this point on, every time any key is pressed, the keyboard library immediately executes the keyboard_event function, passing it the event information as the event argument.

4. User Notification
print(“Keylogger running, press ‘Ctrl’ to stop execution”)
This line informs the user that keylogging has started and tells them which key (Ctrl) to press to stop execution.

5. Blocking and Waiting for Termination
keyboard.wait(‘ctrl’)
The keyboard.wait(‘ctrl’) command is a blocking call.
It stops the execution of the main script and instructs the program to wait indefinitely until the specified key is pressed, in this case, the Ctrl key.
