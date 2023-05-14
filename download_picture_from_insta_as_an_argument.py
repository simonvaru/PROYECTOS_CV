# In this code, we use the requests library to send GET requests to the Instagram post URL and
# retrieve the HTML content. Then, we utilize the BeautifulSoup library to parse the HTML and
# find the <meta> tag containing the image URL. Once we have the image URL, we send another
# GET request to download the image content and save it to a file.
# 
# Remember to replace "https://www.instagram.com/p/EXAMPLE_POST_LINK/" with the actual
# Instagram post link you want to download the image from.

#example: python.exe ./open_url_5.py 'https://www.instagram.com/p/CsL5gwKM4Hn/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='



import requests
from bs4 import BeautifulSoup
import hashlib
import time
import sys

# Accessing command-line arguments
arguments = sys.argv

# The first argument (index 0) is the program filename
program_name = arguments[0]

# The subsequent arguments are the ones passed through the terminal
# Access them using their respective indices
argument1 = arguments[1]


def generate_unique_filename():
    # Generate a unique file name using MD5 hash of the current timestamp
    timestamp = str(time.time()).encode('utf-8')
    hashed = hashlib.md5(timestamp).hexdigest()
    return hashed

def download_instagram_image(post_link):
    # Send a GET request to the Instagram post URL
    response = requests.get(post_link)

    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the <meta> tag containing the image URL
        meta_tag = soup.find('meta', property='og:image')

        if meta_tag:
            image_url = meta_tag['content']

            # Send a GET request to download the image
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                # Extract the image file name from the URL
                file_name = generate_unique_filename() + '.jpg' 
                

                # Save the image to a file
                with open(file_name, 'wb') as f:
                    f.write(image_response.content)
                print("Image saved successfully.")
            else:
                print("Failed to download the image.")
        else:
            print("Image URL not found in the provided link.")
    else:
        print("Failed to fetch the Instagram post.")

# Example usage
post_link = argument1
download_instagram_image(post_link)
