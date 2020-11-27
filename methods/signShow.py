import os

shpfiles = []
import cv2


path = 'C:\\Users\\shaheen\\Desktop\\input-sign\\'

fullpath=''
def signRecog(self,text):

    with os.scandir(path) as entries:
        for entry in entries:
            name = entry.name
            #print('aaaa', name)
            head_tail = os.path.split(name)
            fullpath = os.path.join(path + name)
            f = head_tail[0]
            #print('f ', f)

            print('file ', fullpath)
            print('name ', name)
            print('speech ', text)
            fname=name.split(".")
            fn=fname[0]

            if (fn in text):
               # print('we', name)
                print("text is :", text)
                img1 = cv2.imread(fullpath)
                font = cv2.FONT_HERSHEY_SIMPLEX

                # org
                org = (30, 30)

                # fontScale
                fontScale = 0.7

                # Blue color in BGR
                color = (255, 51, 51)

                # Line thickness of 2 px
                thickness = 1
                # new_image=cv2.resizeWindow('img', 600, 600)

                # define the screen resulation
                screen_res = 600, 800
                scale_width = screen_res[0] / img1.shape[1]
                scale_height = screen_res[1] / img1.shape[0]
                scale = min(scale_width, scale_height)

                # resized window width and height
                window_width = int(img1.shape[1] * scale)
                window_height = int(img1.shape[0] * scale)

                # cv2.WINDOW_NORMAL makes the output window resizealbe
                cv2.namedWindow('Result Window', cv2.WINDOW_NORMAL)

                # resize the window according to the screen resolution
                cv2.resizeWindow('Result Window', window_width, window_height)

                # Using cv2.putText() method
                image1 = cv2.putText(img1, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

                # Displaying the image
                cv2.imshow('Result Window', image1)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            else:
                print("does not get related sign images ....")