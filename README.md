# PyThaiStock
- A simple python program to access data from SiamChart and SET Thailand
- <img src="images/PyThaiStock v0.1.png" alt="PyThaiStock" width="50%" height="50%">
- Download here:  [Release ](https://github.com/kcommerce/PyThaiStock/releases/)  
# Credits:
- SiamChart: www.siamchart.com
- SET Thailand: www.set.or.th

# Prerequisites
- MacOS
- Python 3+


  
### Build executable on MacOS
- Install pyinstaller
  ```bash
  pip install pyinstaller
  ```
- Run the following command to build :
  ```bash
  pyinstaller --noconsole --onefile web.py
  ```
### Create DMG installer on MacOS
- Reference : https://medium.com/@jackhuang.wz/in-just-two-steps-you-can-turn-a-python-script-into-a-macos-application-installer-6e21bce2ee71
- Reference: https://github.com/create-dmg/create-dmg
- Install create-dmg command from brew:
  ```bash
  brew install create-dmg
  ```
- Run the following command :
  ```bash
  create-dmg --volname "PyThaiStock" --window-pos 200 120 --window-size 600 300 --hide-extension web.app --app-drop-link 425 120 "PyThaiStock.dmg" "dist"
  ```
