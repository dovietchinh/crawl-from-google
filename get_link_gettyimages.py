import requests
import os
import io 
from PIL import Image
import hashlib
from tqdm import tqdm
def main():
    IMAGES_PER_TERM = 100
    with open('search_terms.txt') as f:
        search_terms = f.readlines()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    template = 'class="MosaicAsset-module__thumb___epLhd" src'
    len_ = len(template)
    bar_plot = tqdm(total=IMAGES_PER_TERM,desc='get link')
    for q in search_terms:
        links = []
        q = q.strip().replace(' ','%20')
        for page in range(1,100):
            urls = f'https://www.gettyimages.com/photos/old-man-full-body?assettype=image&sort=mostpopular&phrase={q}&page={page}'
            response = requests.get(urls,headers=headers)
            if not response.ok:
                break
            html = response.text
            index = html.find(template)
            html = html[index+len_+2:]
            index = html.find('\"')
            links.append(html[:index])
            bar_plot.update(1)
            if len(links) >= IMAGES_PER_TERM:
                break
        for link in tqdm(links,desc='get images'):
            r = requests.get(link)
            if not r.ok:
                continue
            image_content = r.content
            filename = hashlib.sha1(image_content).hexdigest()[:10] + '.jpg'
            file_path = os.path.join('download', filename)
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=95)
                
                


if __name__ =='__main__':
    main()

