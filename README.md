# 目的

I2C接続のセンサ郡より値を取得する

# 取得対象とするセンサ群

+ INA226  
電圧/電流/電力を取得 バッテリ管理を実施するため
+ LSM303DLHC  
地磁気/加速度を取得するため

# 実行方法

値の取得ができるか/適正値かユニットテストを用意しています。
```
# ./i2c_sensor_test.py
```

# 参考ソース

下記を参考に開発しました、ありがとうございました。

## 参考リンク

http://green-rabbit.sakura.ne.jp/note/2014/08/24/beaglebone-black-power-meter-soft/
http://airwhite.net/?p=347

## 利用ライブラリ

https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code