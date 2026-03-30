import requests

url = "http://localhost:5000/api/predict"
image_path = r"E:\workspace\ML\Bangladesh\BAIUST\posture (2)\posture\Image_1000.jpg"

with open(image_path, "rb") as f:
    files = {"image": f}
    response = requests.post(url, files=files)

print(response.json())