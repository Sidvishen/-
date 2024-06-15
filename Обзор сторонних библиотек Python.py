# import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# r.status_code
# 200
# r.headers['content-type']
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
# r.text
# '{"type":"User"...'
# r.json()
# {'private_gists': 419, 'total_private_repos': 77,}
# print(r.text)

# import pandas as pd
# data = pd.read_csv('data.csv')
# print(data.describe())

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# result = np.sum(arr)
# print(result)

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.show()
#
# from PIL import Image
# img = Image.open('image.jpg')
# resized_img = img.resize((300, 300))
# resized_img.save('new_image.jpg')