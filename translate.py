import cv2 as cv
import numpy as np
import os
from time import time
import easyocr
from kakaotrans import Translator
from PIL import ImageFont, ImageDraw, Image

class trans:
    def __init__(self):
        self.reader = easyocr.Reader(['en']);
        self.translator= Translator()
        pass
    
    def draw_text(self,image, bounds,color = 'yellow',width=2):
        img = Image.fromarray(image)
        draw = ImageDraw.Draw(img)
        font=ImageFont.truetype("fonts/gulim.ttc",15)
        for bound  in bounds:
            (top_left, top_right, bottom_right, bottom_left)=bound[0]
            text = bound[1];
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
            size = font.getsize(text)
            fontimg = Image.new('RGB', size=size, color=(0, 0, 0))
            fontdraw = ImageDraw.Draw(fontimg)
            fontdraw.text((0, 0), text, fill=(209, 239, 8), font=font)
            img.paste(fontimg,top_left)
    
        image=np.array(img)
        return image

    def draw_box(self,image, bounds,color = 'yellow',width=2):
        for bound  in bounds:
            (top_left, top_right, bottom_right, bottom_left)=bound[0]
            text = bound[1];
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            cv.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(0, 255, 255), thickness=1)

    def run(self,path,q):
        loop_time = time()
        screenshot = cv.imread(path)
        bounds = self.reader.readtext(screenshot)
        print("번역완료")
        bounds_ko = []
        for bound  in bounds:
            text = bound[1]
            try:
                text_ko = self.translator.translate(text,src='en',tgt='kr')
            except:
                pass
            y = list(bound)
            y[1] = text_ko
            bounds_ko.append(tuple(y))
        self.draw_box(screenshot,bounds_ko)
        print("박스 그리기 완료")
        screenshot=self.draw_text(screenshot,bounds_ko)
        print("텍스트 그리기 완료")
        fps='FPS {}'.format(1 / (time() - loop_time))
        cv.putText(screenshot, fps, (0, 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv.imshow('Computer Vision', screenshot)
        q.put(0)
        cv.waitKey(0)
        cv.destroyWindow('Computer Vision')
        print("끝")





