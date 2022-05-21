import os
import cv2
import shutil
def get_unique_image():
	with open('asd.txt') as f:
		lines = f.readlines()
	abc = dict()
	abcd = []
	for line in lines:
		line = line.strip()
		base_name = os.path.basename(line)
		if not hasattr(abc,base_name):
			abc[base_name] = [line]
		else:
			abc[base_name].append(line)
	for k,v in abc.items():
		abcd.append(v[0]+'\n')
	with open('asd_new.txt','w') as f:
		f.writelines(abcd)

def main():
	files = os.listdir('/u01/Intern/chinhdv/github/google_image_download/yte_detect/crops/person')
	for file in files:
		path = os.path.join('/u01/Intern/chinhdv/github/google_image_download/yte_detect/crops/person',file)
		img = cv2.imread(path)
		size = img.shape[0]+img.shape[1]
		if size < 120 or img.shape[0]<30 or img.shape[1]<30:
			new_name = os.path.join('b',file)
			os.rename(path,new_name)
def main2():
	for root,dirs,files in os.walk('yte_detect'):
		for file in files:
			path = os.path.join(root,file)
			new_name = os.path.join('total',file)
			os.rename(path,new_name)
if __name__ =='__main__':
	main2()
		
	
		
