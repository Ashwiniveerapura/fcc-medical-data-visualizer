import urllib.request

url = "https://freecodecamp.org"
urllib.request.urlretrieve(url, "medical_examination.csv")
print("Dataset file created and written successfully!")
