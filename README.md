# pxsrt

### Requiremets:
Python3:
<https://wiki.python.org/moin/BeginnersGuide/Download>

Installation:
```
git clone https://github.com/oprince-tech/pxsrt.git
cd pxsrt
pip3 install .
```
Installing into a virtual environment (alternate):
```
git clone https://github.com/oprince-tech/pxsrt.git
cd pxsrt
python3 -m venv venv
source venv/bin/active
pip3 install .
```
### Usage (shell):
```
pxsrt <Image> [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-o] [-r] [-p] [-s] [-h]
```
### Usage (package):
```
from pxsrt.main import pxsrt

pxsrt(<Image> [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-o] [-r])
```
E.g.:
```
pxsrt('tokyo.jpg', mode='S', direction='v', l_threshold=100, u_threshold=200, outer=True)
returns => <PIL.Image.Image image mode=RGB size=750x500 at 0x7FC992DEE8E0>
```

### Notes:
|Option  |Description|
|--------|------------------------------|
|Image   |Place the file you wish to sort in the Images folder|
|-m      |Mode (H/S/V) or (R/G/B) [defaults to V]|
|-d      |Direction (v or h) [defaults to h]|
|-t      |Threshold (2 value between 0 and 255) [defaults to 0 255]|
|-r      |Reverse (reverse the order pixels are sorted)|
|-o      |Outer (sort the pixels outside of your threshold range)|
|-p      |Preview (display preview of threshold map)|
|-s      |Save (save image)|

### Examples:
*Before images can be found in the Images folder*
```
pxsrt tokyo.jpg -d v -t 0 50 -r
```
![tokyo_Pv50ru.jpg](https://github.com/oprince-tech/pxsrt/blob/master/images/tokyo_Pv50ru.jpg)
___

```
pxsrt koi.jpg -d v -r
```
![koi_Pv255r.jpg](https://github.com/oprince-tech/pxsrt/blob/master/images/koi_Pv255r.jpg)
___

```
pxsrt street,jpg -d h -t 0 40 -r
```
![street_Ph40ru.jpg](https://github.com/oprince-tech/pxsrt/blob/master/images/street_Ph40ru.jpg)
___

```
pxsrt sakura.jpg -r
```
![sakura_Ph255r.jpg](https://github.com/oprince-tech/pxsrt/blob/master/images/sakura_Ph255r.jpg)
