import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

hinh1 = """
      * 
      * *
      * * *
* * * * * * *
* * *
* *
*
"""

hinh2 = """
      * 
      * *
      *   *
* * * * * * *
*   *
* *
*
"""

hinh3 = """
      * * * *
      * * * 
      * *
      *
    * *
  * * *
* * * * 
"""

hinh4 = """
      * * * *
      *   * 
      * *
      *
    * *
  *   *
* * * * 
"""

ds_hinh = [hinh1, hinh2, hinh3, hinh4]

for h in ds_hinh:
    # clear()
    print(h)
    time.sleep(5)
