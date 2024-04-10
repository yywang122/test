import cv2
import numpy as np
import pytesseract
import re
import csv
import os
'''
# 定義提取文本的函數
def extract_text(image_path, num_contours):
    # 讀取圖片
    image = cv2.imread(image_path)
    # 將圖片轉換為灰度
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化處理
    _, binary_image = cv2.threshold(gray_image, 249, 255, cv2.THRESH_BINARY)
    # 尋找連續區域
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 找到最大的連續區域
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[1:num_contours]
    contours = sorted(sorted_contours, key=lambda x: cv2.boundingRect(x)[0])
    extracted_texts = []
    # 遍歷每個區域並應用OCR
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = binary_image[y:y+h, x:x+w]
        # 裁剪區域
        cropped_region = image[y:y+h, x:x+w]
        inverted_roi = cv2.bitwise_not(cropped_region)
        inverted_roi2 = cv2.threshold(cv2.cvtColor(inverted_roi, cv2.COLOR_BGR2GRAY), 170, 225, cv2.THRESH_BINARY_INV)[1]
        text = pytesseract.image_to_string(inverted_roi2, lang='eng', config='--psm 10')  # 使用PSM 6參數處理單一塊文字
        # 使用正則表達式提取 "mm" 之前的數值，並保留小數點前一位
        match = re.search(r'\d\.\d{1,3}', text)
        if match:
            text = match.group()
        extracted_texts.append(text)
    return extracted_texts

# 主目錄路徑
main_directory = './test'

# 處理每個子目錄
for subdir, _, _ in sorted(os.walk(main_directory)):
    # 子目錄下的圖片檔案列表
    image_files = sorted([f for f in os.listdir(subdir) if f.endswith('.jpg')])
    # 定義存儲提取文本的列表
    extracted_texts_list = []
    # 處理每張圖片
    for image_file in image_files:
        image_path = os.path.join(subdir, image_file)
        # 提取文本
        num_contours = 6 if 'OCP' in subdir else 4
        if num_contours != 0:
            extracted_texts = extract_text(image_path, num_contours)
            # 添加圖片名稱和文本到列表中
            extracted_texts_list.append([image_file] + extracted_texts)
    # 如果有提取到文本，則寫入 CSV 檔案
    if extracted_texts_list:
        csv_file_name = os.path.basename(subdir) + '.csv'
        csv_file_path = os.path.join(subdir, csv_file_name)
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Image Name', '[1]', '[2]', '[3]' if 'IQC' in subdir else '[3]', '[4]', '[5]'])  # 寫入列標題
            writer.writerows(extracted_texts_list)

        print(f'Processed {subdir} and saved extracted texts to {csv_file_path}')'''
