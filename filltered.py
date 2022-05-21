import os 
import shutil

dict_ = {}
for root,dirs,files in os.walk('images'):
    for file in files:
        path = os.path.join(root,file)
        base = os.path.basename(path)
        if dict_.get(base) is None:
            dict_[base] = [path]
        else:
            os.remove(path)

