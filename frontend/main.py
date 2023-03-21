import os
import eel
from random import randint
  
eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/templates')  
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)
  
# Start the index.html file
eel.start("index.html", size=(1000, 1000))