import pyautogui, cv2
'''
自動使用計算機補充: 此時計算機應該明顯出現在桌面上，不然會有判斷錯誤的問題  設定 confidence 是為了解決圖像誤差的問題（可參考 OpenCV 關於 confidence 的說明）。由於每個人電腦的解析度與色彩設定不盡相同，若是將按鈕截圖與他人分享，可能會造成辨識上的誤差，此時可以修改該值，來完成比對；如果還是無法正常比對，建議自行截圖，此時圖片最接近本機的設定。
refer to: https://www.cc.ntu.edu.tw/chinese/epaper/home/20220920_006203.html
'''

# 設定每一個動作，都暫停若干秒
pyautogui.PAUSE = 0.1
# 比對所有圖片，取得顯示在桌面的圖片物件
btn_0_location = pyautogui.locateOnScreen('images/0.png', confidence=0.9)
btn_1_location = pyautogui.locateOnScreen('images/1.png', confidence=0.9)
btn_2_location = pyautogui.locateOnScreen('images/2.png', confidence=0.9)
btn_3_location = pyautogui.locateOnScreen('images/3.png', confidence=0.9)
btn_5_location = pyautogui.locateOnScreen('images/5.png', confidence=0.9)
btn_6_location = pyautogui.locateOnScreen('images/6.png', confidence=0.9)
btn_7_location = pyautogui.locateOnScreen('images/7.png', confidence=0.9)
btn_8_location = pyautogui.locateOnScreen('images/8.png', confidence=0.9)
btn_plus_location = pyautogui.locateOnScreen('images/plus.png', confidence=0.9)
btn_multiply_location = pyautogui.locateOnScreen('images/multiply.png', confidence=0.9)
btn_subtract_location = pyautogui.locateOnScreen('images/subtract.png', confidence=0.9)
btn_equal_location = pyautogui.locateOnScreen('images/equal.png', confidence=0.9)
btn_dot_location = pyautogui.locateOnScreen('images/dot.png', confidence=0.9)
# 取得每一個圖片的座標資訊
btn_0_point = pyautogui.center(btn_0_location)
btn_1_point = pyautogui.center(btn_1_location)
btn_2_point = pyautogui.center(btn_2_location)
btn_3_point = pyautogui.center(btn_3_location)
btn_5_point = pyautogui.center(btn_5_location)
btn_6_point = pyautogui.center(btn_6_location)
btn_7_point = pyautogui.center(btn_7_location)
btn_8_point = pyautogui.center(btn_8_location)
# 取得每一個圖片的中心點
btn_plus_point = pyautogui.center(btn_plus_location)
btn_subtract_point = pyautogui.center(btn_subtract_location)
btn_multiply_point = pyautogui.center(btn_multiply_location)
btn_equal_point = pyautogui.center(btn_equal_location)
btn_dot_point = pyautogui.center(btn_dot_location)
# 按下 250
pyautogui.click(btn_2_point.x, btn_2_point.y)
pyautogui.click(btn_5_point.x, btn_5_point.y)
pyautogui.click(btn_0_point.x, btn_0_point.y)
# 按下 x
pyautogui.click(btn_multiply_point.x, btn_multiply_point.y)
# 按下 2
pyautogui.click(btn_2_point.x, btn_2_point.y)
# 按下 +
pyautogui.click(btn_plus_point.x, btn_plus_point.y)
# 按下 38
pyautogui.click(btn_3_point.x, btn_3_point.y)
pyautogui.click(btn_8_point.x, btn_8_point.y)
# 按下 -
pyautogui.click(btn_subtract_point.x, btn_subtract_point.y)
# 按下 17.8686
pyautogui.click(btn_1_point.x, btn_1_point.y)
pyautogui.click(btn_7_point.x, btn_7_point.y)
pyautogui.click(btn_dot_point.x, btn_dot_point.y)
pyautogui.click(btn_8_point.x, btn_8_point.y)
pyautogui.click(btn_6_point.x, btn_6_point.y)
pyautogui.click(btn_8_point.x, btn_8_point.y)
pyautogui.click(btn_6_point.x, btn_6_point.y)
# 按下 =
pyautogui.click(btn_equal_point.x, btn_equal_point.y)
