import pyautogui
import keyboard
'''
    打擊遊戲
    範例網址: https://taiko.bui.pm/ not worked
    範例網址: https://ouo.269seahorse.me/
    （請先取得參考用的座標、色碼）
            Red, Green, Blue
    橘色圖示: (243, 71, 40)
    藍色圖示: (101, 189, 187)
    連打區域: (243, 181, 0)
    滑鼠定點: (x=519, y=455)
    refer to: https://www.cc.ntu.edu.tw/chinese/epaper/home/20220920_006203.html
'''

# 設定每一個動作後，都暫停若干秒
pyautogui.PAUSE = 0.1

# 固定打擊點 01
listPoint01 = [519, 455]

# 點擊
def click():
    # 每次點擊都會重新取得滑鼠定點的 RGB 值
    coord01 = pyautogui.pixel( listPoint01[0], listPoint01[1] )
    # [0] 代表 Red，[1] 代表 Green，[2] 代表 Blue
    if coord01[0] == 243 and coord01[1] == 71: # 若 R = 243, G = 71
        pyautogui.press('j') # 右邊內側橘色
    elif coord01[0] == 101 and coord01[1] == 189: # 若 R = 101, G = 189
        pyautogui.press('k') # 右邊外側藍色
    elif coord01[0] == 243 and coord01[1] == 181: # 若 R = 243, G = 181
        pyautogui.press('d') # 左邊外側藍色
        pyautogui.press('f') # 左邊內側橘色
        pyautogui.press('j') # 右邊內側橘色
        pyautogui.press('k') # 右邊外側藍色


'''
主程式區域
'''
if __name__ == "__main__":
    while True:
        # 當我們按下 ctrl 鍵時，自動點擊
        if keyboard.is_pressed('ctrl'):
            click()
