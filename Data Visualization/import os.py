import os
import time
import pyfiglet
file_name = "temp.txt"
file_content = "SHAMAN   IS   GOOD   BOY"

with open(file_name, 'w') as f:
    f.write(file_content)
print("File content:")
text = pyfiglet.figlet_format(file_content)
print(text)

print(f"File will be deleted in 10 seconds...")
for i in range(10, 0, -1):
    print(f"{i}...")
    time.sleep(1)

os.remove(file_name)
print(f"NOooooooo......")
print(f"'{file_name}' has been deleted.")
print(f"But shaman is still pedo :/")
