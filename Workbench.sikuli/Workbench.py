import glob
import os

for f in glob.glob('**/.class', recursive=True):
    os.remove(f)

import os

dir = os.getcwd()+"\\Workbench.sikuli\\Classes"
print dir

for root, dirs, files in os.walk(dir):
  for name in files:
    if name.endswith((".class")):
      os.remove(os.path.join(root, name))

import os
print os.getcwd()

import shutil

click("Btn_Work.png")
click("SubHeading_Batches_Batch.png")
click("DropDownBtn_Batches_Batch.png")
type(Key.DOWN)
    
#Copy the batch name already selected
type("c", KEY_CTRL)
batchNameCopied = Env.getClipboard()

print batchNameCopied

import clipboard
test = clipboard.paste()
print test