from PyQt5.QtGui import QIntValidator


# 这个有问题，不能正确限制大小，只能限制位数
range_24 = QIntValidator()
range_24.setRange(0, 24)

range_60 = QIntValidator()
range_60.setRange(0, 60)

range_99 = QIntValidator()
range_99.setRange(0, 99)

range_9999 = QIntValidator()
range_9999.setRange(0, 9999)


power_by = r'''
             /)  (\
       .-._((,~~.))_.-,         //"""/""/
        `-.   @@   ,-'       //     /  /
          / ,o--o. \         //╲   /  /
         ( ( .__.   ) )      //   ╲/,,/
          ) `----'   (     //
         /              \  ()
       /                  \//
     /                      \
power by 战斧奶牛

https://www.52pojie.cn/thread-1645599-1-1.html

https://github.com/zhaoxinyuan996/auto-shutdown-py'''
