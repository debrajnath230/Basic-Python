import re
import requests
import os

user = input('Enter the search image: ')

user_agent = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = f'https://www.google.com/search?q={user}&sca_esv=595369570&rlz=1C1GCCJ_en&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiyoevr2cGDAxWdbWwGHYT6Ci0Q_AUoAXoECAIQAw&biw=1536&bih=714&dpr=1.25'

response = requests.get(url=url, headers=user_agent).text

# Use a more robust pattern to match image URLs
pattern = r'\["(https://.*?\.jpg)",[0-9]+,[0-9]+\]'
images = re.findall(pattern, response)

print(f"total images : {len(images)}")

no_of_images = int(input("Number of images to be downloaded: "))

# Check if the directory exists, create it if it doesn't
if not os.path.exists(user):
    os.mkdir(user)

# Change the current working directory to the created/found directory
os.chdir(user)

# Loop through the specified number of images and download them
for i, image_url in enumerate(images[:no_of_images], start=1):
    print(f"Downloading image {i} of {no_of_images}")
    try:
        response = requests.get(url=image_url)
        # Ensure the request was successful before saving the image
        if response.status_code == 200:
            with open(f"{user}_{i}.jpg", 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f"Error downloading image {i}: {e}")
