#coding=utf-8
import random
import string
import sys
import math
#from train import *
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
#生成几位数的验证码
number = 7
#生成验证码图片的高度和宽度
size = (190,40)
#背景颜色，默认为白色
bgcolor = (0,0,255)
#字体颜色，默认为蓝色
fontcolor = (255,255,255)
#干扰线颜色。默认为红色
linecolor = (255,0,0)
#是否要加入干扰线
draw_line = False
draw_point = True
#加入干扰线条数的上下限
line_number = (1,5)
 
#用来随机生成一个字符串
number = ['0','1','2','3','4','5','6','7','8','9']
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Province = ['京', '津', '沪', '渝', '冀', '豫', '云', '辽', '黑', '湘', '皖', '鲁', '新', '苏', '浙', '赣', '鄂', '桂', '甘', '晋', '蒙', '陕',
'吉', '闽', '贵', '粤', '青', '藏', '川', '宁', '琼']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 验证码一般都无视大小写；验证码长度4个字符
def gene_text(char_set=number+ALPHABET, captcha_size=7):
    captcha_text = []
    captcha_text.append(random.choice(Province))
    captcha_text.append(random.choice(ALPHABET))
    captcha_text.append(' · ')
    for i in range(2,captcha_size):
    	c = random.choice(char_set)
    	captcha_text.append(c)
    return ''.join(captcha_text)
#用来绘制干扰线
def gene_line(draw,width,height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill = linecolor)
def rotate(img):
        rot = img.rotate(random.randint(-15,15),expand=0) #默认为0，表示剪裁掉伸到画板外面的部分
        fff = Image.new('RGB',rot.size,(255,)*4)
        return Image.composite(rot,fff,rot)
#生成验证码
def create_points(draw,width,height):
        '''绘制干扰点'''
        #chance = min(100, max(0, 100)) # 大小限制在[0, 100]  # 设置干扰点在所有点中所占比例
        chance = 5
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                #print(tmp)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))  # 满足条件的点就给打成黑色

def gene_code():
    width,height = size #宽和高
    image = Image.new('RGBA',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype('./simhei.ttf',32) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    text = gene_text() #生成字符串
    font_width, font_height = font.getsize(text)
    number = 7
    draw.text(((width - font_width) / number, (height - font_height) / number),text,
            font= font,fill=fontcolor) #填充字符串、
    
    if draw_line:
        gene_line(draw,width,height)
    if draw_point:
        create_points(draw,width,height)
    #image = rotate(image)
    #image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    text = text.replace('·','')
    img = image.convert('L')
    #img.save('%s.png' % text)
    return text,np.array(img)
    
def gen_captcha_text_and_image():
    captcha_text,captcha = gene_code()
	#image.write(captcha_text, captcha_text + '.jpg')  # 写到文件
    #captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha)
    return captcha_text, captcha_image
def convert2gray(img):
    I = Image.open(img)
    I.show()
    L = I.convert('L')   #转化为灰度图
    
    #L = I.convert('1')   #转化为二值化图
    L.show()
def gen_image(text):
    width,height = size #宽和高
    image = Image.new('RGBA',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype('./msyh.ttf',32) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    font_width, font_height = font.getsize(text)
    number = 7
    draw.text(((width - font_width) / number, (height - font_height) / number),text,
            font= font,fill=fontcolor) #填充字符串、
    if draw_line:
        gene_line(draw,width,height)
    if draw_point:
        create_points(draw,width,height)
    #image = rotate(image)
    #image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    text = text.replace('·','')
    img = image.convert('L')
    img.save('%s.png' % text)
    return img
if __name__ == "__main__":
    #gene_code()
    #convert2gray("timg.jpeg")
    gen_image("京·PH3X00")