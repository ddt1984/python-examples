# 맥북 이미지와 로고 이미지 합쳐서 새로운 이미지 만드는 코드
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def resize(image, perecent):
    return image.resize((int(image.size[0] * perecent), int(image.size[1] * perecent)), Image.HAMMING)

# 이미지 파일 로딩
macImage = Image.open("samples/apple-macbook.png")
pythonImage = Image.open("samples/python-logo.png")
pythonImage = resize(pythonImage, 0.4) #로고 사이즈가 커서 40%로 줄임

# 이미지를 합치기 전에 로고 이미지가 들어갈 위치 계산
# 맥북 이미지 중안에 오도록 하는 코드
x = int(macImage.size[0] / 2 - (pythonImage.size[0] / 2))
y = int(macImage.size[1] / 2 - (pythonImage.size[1] / 2))
macImage.paste(pythonImage, (x, y), pythonImage) # 이미지 붙이기

newImg = Image.new("RGBA", macImage.size, 0)
newImg.paste(macImage, (0, 0))

# 문자열도 추가하는 코드
font = ImageFont.truetype("consola.ttf", 30) # 폰트와 사이즈 
imgEditable = ImageDraw.Draw(newImg)
textX = x + 10
textY = y + pythonImage.size[1] + 15
text = ">> Hello world"
color = (0, 0, 0) # black 
imgEditable.text((textX, textY), text, color, font)

newImg.save("samples/mac-and-python.png", 'PNG')