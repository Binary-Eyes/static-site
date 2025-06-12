import os
import shutil

print("static site generator v1.0.0")
print("developed by: amir barak")

public_path = os.path.join(os.curdir, "public")
if os.path.exists(public_path):
    print("deleting public")
    shutil.rmtree(public_path)



print("goodbye")
