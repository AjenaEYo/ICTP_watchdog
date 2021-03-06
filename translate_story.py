import cv2 as cv
import numpy as np
import os
from time import time
import easyocr
from kakaotrans import Translator
from PIL import ImageFont, ImageDraw, Image
import textwrap
class trans_story:
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
    
    def draw_text_story(self,image, bounds,text):
        img = Image.fromarray(image)
        font=ImageFont.truetype("fonts/gulim.ttc",15)
        (top_left, top_right, bottom_right, bottom_left)=bounds[0][0]
        #top_left = (int(top_left[0]), int(top_left[1]))
        top_left = (int(top_left[0]), int(img.height))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        size = font.getsize(text)
        lines = textwrap.wrap(text, width=40)  
        size = (size[0],size[1]*len(lines)) 
        # y = list(size)
        # y[1] = size[1]*len(lines)
        # size = tuple(y)

        fontimg = Image.new('RGB', size=size, color=(0, 0, 0))
        fontdraw = ImageDraw.Draw(fontimg)

        image1_size = img.size
        image2_size = fontimg.size
       
        y_text = 0
        w_x= []
        w_x.append(image1_size[0])
        for line in lines:
            line_width, line_height = font.getsize(line)
            fontdraw.text((0, y_text), 
                    line, font=font, fill=(209, 239, 8))
            # fontdraw.text(((image1_size[0] - line_width) / 2, y_text), 
            #         line, font=font, fill=(209, 239, 8))
            y_text += line_height
            w_x.append(line_width)
        #fontdraw.text((0, 0), text, fill=(209, 239, 8), font=font)
        
        img_w = max(w_x)
        print(img_w)
        new_image = Image.new('RGB',(img_w, image1_size[1]+image2_size[1]), (250,250,250))
        new_image.paste(img,(0,0))
        new_image.paste(fontimg,(0,image1_size[1]))
        image=np.array(new_image)
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
        #text_list = self.reader.readtext(screenshot,detail=0)
        text_list=[]
        for bound in bounds:
            text_list.append(bound[1])
        
        text_comb=''.join(text_list)
        text_ko = self.translator.translate(text_comb,src='en',tgt='kr')
        print(text_ko)
        print("????????????")
        self.draw_box(screenshot,bounds)
        print("?????? ????????? ??????")
        screenshot=self.draw_text_story(screenshot,bounds,text_ko)
        print("????????? ????????? ??????")
        fps='FPS {}'.format(1 / (time() - loop_time))
        cv.putText(screenshot, fps, (0, 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv.imshow(os.path.basename(path), screenshot)
        q.put(0)
        cv.waitKey(0)
        cv.destroyWindow(os.path.basename(path))
        print("???")





