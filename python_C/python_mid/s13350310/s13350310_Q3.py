#Q3 給一個整數n計算其位數的總和

test_input = 1234
total = 0       #令加總原始值為0

for i in str(test_input):       #將test_input轉成字串並依序偵測
    total += int(i)     #將偵測到的字串轉為整數加到total

print(total)

#結果為10

