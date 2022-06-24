from urllib import request
import time
import PIL.Image
import io

url = "https://th.bing.com/th/id/R.92c0a7443c6f543a60d18e1b964e6429?rik=5HIjq%2fxf7wRBAw&riu=http%3a%2f%2fup.gc-img.net%2fpost_img%2f2017%2f12%2fYqbszZgCyo5xqa4_Udzfb_1483.jpeg&ehk=oryFScxMP%2bR1goeEHfWcr6jLLo4A1RcSGNtilzv3Ing%3d&risl=&pid=ImgRaw&r=0"

# time check
start = time.time()

# request.urlopen()
res = request.urlopen(url).read()

# 이미지 다운로드 시간 체크
print(time.time() - start)


# Image open
img = PIL.Image.open(io.BytesIO(res))