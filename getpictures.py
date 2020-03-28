#download pictures from a webpage
import requests
from bs4 import BeautifulSoup as bs
import os

# #url website with pictures
# url  = "https://innovateinfinitely.com/"
# #download website for parsing
# page = requests.get(url)
# soup = bs(page.text, "html.parser")
# #print(page) #print <Response [200]>
# #print(soup) #print the html code
# #locate all elements with image tag or <img>
# imagetags = soup.findAll("img")
# #print(imagetags) #print html code with <img>
# #create directory for pictures
# if not os.path.exists("pictures"):
# 	os.makedirs("pictures")
# #change directory to copy pictures to the changed directory
# os.chdir("pictures")
# #picture file name number variable
# x = 0
# #write images to directory
# for eachimagetags in imagetags:
# 	try:
# 		url = eachimagetags["src"]
# 		print("url "+url)
# 		source = eachimagetags.get(url)
# 		print("source "+source)
# 		#if source.status_code == 200:
# 		with open(os.path.basename(url),"wb") as picturefile:
# 			print(x)
# 			picturefile.write(requests.get(url).content)
# 			picturefile.close()
# 			x += 1
# 	except:
# 		pass

#https://stackoverflow.com/questions/54338681/how-to-download-images-from-websites-using-beautiful-soup
from PIL import Image
url  = "https://innovateinfinitely.com/"
response = requests.get(url)
soup = bs(response.text,"html.parser")
getimage = soup.find("img")
getimageurl = getimage["src"]
print(getimage) #print <img alt="Raymond Mar" src="raymondmarindex.jpg"/>
print(getimageurl) #print raymondmarindex.jpg
#openimage = Image.open(requests.get(getimageurl, stream=True).raw)
#openimage.save("image.jpg")
with open("filename","wb") as saveimage:
	saveimage.write(requests.get(getimageurl).content)
	saveimage.close()

# website with model images
url = 'https://www.pexels.com/search/model/'
# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# locate all elements with image tag
image_tags = soup.findAll('img')
# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')
# move to new directory
os.chdir('models')
# image file name variable
x = 0
# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass