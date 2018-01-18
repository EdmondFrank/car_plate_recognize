# -*- coding: utf-8 -*-

import unittest
from train import *
from gen_plate import *
class TestTrain(unittest.TestCase):
    def setUp(self):
        #print("do something before test.Prepare environment.")
        pass
    def tearDown(self):
        pass
        #print("do something after test.Clean up.")
    def test_vec2text(self):
        """Test method add(a, b)"""
        print("test_vec2text")
        test = text2vec("云F71K64")
        self.assertEqual("云F71K64", vec2text(test))
    def test_text2vec(self):
        print("test_text2vec")
        vec = text2vec("云F71K64")
        self.assertEqual(1, vec[43+68*0])
        self.assertEqual(1, vec[15+68*1])
        self.assertEqual(1, vec[7+68*2])
        self.assertEqual(1, vec[1+68*3])
        self.assertEqual(1, vec[20+68*4])
        self.assertEqual(1, vec[6+68*5])
        self.assertEqual(1, vec[4+68*6])
        #print(vec)
    def test_get_next_batch(self):
        batch_x,batch_y = get_next_batch2(2)
        for i in range(1): 
            #text, image = gene_code()
            text = vec2text(batch_y[i,:])
            #image = gen_image(text)
            #image.save('%s.png' % text)
            #image = np.array(image)
            #image = convert2gray(image) 
            #captcha_image = image.flatten() / 255
            img = np.reshape(batch_x[i,:]*255,(IMAGE_HEIGHT,IMAGE_WIDTH))
            image = Image.fromarray(img)
            image = image.convert('RGB')
            image.save('%s.png' % text)
            #print(np.sum(batch_x[i,:]-captcha_image)) 
            #captcha_image = image.flatten()
            print(text) 
            #predict = tf.argmax(tf.reshape(output, [-1, MAX_NP, CHAR_SET_LEN]), 2) 
            #text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1}) 
            #predict_text = text_list[0]
            #predict_value = vec2text(predict_text) 
            #self.assertEqual(text, predict_text)
    def test_id2text(self):
        self.assertEqual('晋SPHC2M',id2text([56,28,25,17,12,2,22]))

if __name__ == '__main__':
    unittest.main()