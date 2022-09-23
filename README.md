<!-- # 記得寫.gitignore -->

# Raspberry settings before starting
## 設定WiFi
> 需要帶樹莓派的請先設定好Wifi
- SSID：HPS-team6
  - Password：HPS-team6-password

## 固定Hostname 
(這樣才不用還要找IP位置)
1. `sudo raspi-config`
2. 進入`1 System Options`
3. 選擇 `Hostname` 更改好之後重新開機

---
# Use cases

## Core Functions
- 創立使用者的功能(數值輸入錯誤的值)
- 更改使用者資料
- 任意更改machine id
- 手動搜尋食物功能(亂輸入會得到什麼)
- 用戶拿有條碼的東西掃描
- 用戶用食物、水果，測量東西的重量與熱量
- 無法辨識食物種類，跳出改手動輸入

## Test plan(QA test)

- UI是否有閃退的問題
- Linux service自動開起環境
- 秤重值是否能正確抓取
- 螢幕觸控鍵盤是否能正常work
- Barcode掃描問題
- 掃描失敗手動輸入

![](https://memecreator.org/static/images/memes/5201835.jpg)

# Demo video
https://www.youtube.com/watch?v=6truBIo4wFs
