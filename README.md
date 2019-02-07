# RaspberryPi-Sensor-Driver

An android-python program to display Kookye sensor set's real time data from Raspberry Pi, and pass data by tcp socket and display on Android application

On Raspberry side:
1. Connect all sensors by following the link: http://kookye.com/2016/08/01/smart-home-sensor-kit-for-arduinoraspberry-pi/
2. Change the pin number in python class base on your connection
3. Run python socketServer.py on your Raspberry Pi

On Android side:
1. Import whole project to Android Studio
2. Connect phone to same network of your Raspberry Pi
3. Run on a Emulator or real phone
4. Enter the IP of your Raspberry Pi
