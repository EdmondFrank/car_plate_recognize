#coding:utf-8
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np
from train import detect_np_cnn,id2text,CHAR_SET_LEN
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

IMAGE_HEIGHT = 40 # 45
IMAGE_WIDTH =  190
MAX_NP = 7

def deal_image(file):
    image=cv2.imread(file)
    GrayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  
    res=cv2.resize(GrayImage,(IMAGE_WIDTH,IMAGE_HEIGHT),interpolation=cv2.INTER_CUBIC)
    #
    
    #cv2.imshow('image',image)
    #cv2.waitKey(0)
    #cv2.destoryAllWindows()  
    ret,thresh1 = cv2.threshold(res,128,255,cv2.THRESH_BINARY)
    cv2.imwrite("test.png", thresh1)
    # plt.figure(1)
    # plt.imshow(thresh1)
    # plt.show()
    # #cv2.imshow('iker',ret) 
    #cv2.waitKey(0)
    #cv2.destoryAllWindows()
    
    #print(thresh1)
    #out = Image.open(ret).convert('L')  
    return np.array(thresh1)
def predict(image):
    X = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT * IMAGE_WIDTH]) 
    keep_prob = tf.placeholder(tf.float32) 
    output = detect_np_cnn(X, keep_prob) 
    saver = tf.train.Saver()
    with tf.Session() as sess: 
        sess.run(tf.global_variables_initializer()) 
        saver.restore(sess, tf.train.latest_checkpoint('./model/')) 
        captcha_image = image.flatten() / 255 
        #captcha_image = image.flatten() 
        predict = tf.argmax(tf.reshape(output, [-1, MAX_NP, CHAR_SET_LEN]),2) 
        text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})
        #print(text_list) 
        predict_text = text_list[0]
        predict_value = id2text(predict_text) 
        print(predict_value)

if __name__=="__main__":
    predict(deal_image("test6.png"))