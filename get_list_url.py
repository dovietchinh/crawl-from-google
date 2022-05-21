import glob
import os

if __name__ == '__main__':

    image_to_url_fn = 'filename_to_url.txt'
    image_folder = 'image_to_search'

    all_image_name = [os.path.split(fn)[-1] for fn in glob.glob(os.path.join(image_folder, '*.jpg'))]
    # print(all_image_name)
    img2url = dict()
    all_url = []
    with open(image_to_url_fn) as fi:
        for line in fi:
            line = line.strip()
            if line:
                img_name, img_url = line.split('\t')
                img_name = img_name.strip()
                img_url = img_url.strip()
                img2url[img_name] = img_url

    with open('all_url.txt', 'w') as fo:
        for img_name in all_image_name:
            if img_name in img2url:
                url = img2url[img_name]
                fo.write(url + '\n')
