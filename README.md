# auto-shutdown-py
## 注意事项

### 添加win10白名单

下面有5张图，需要把整个文件夹都添加到白名单，因为main.exe和auto_job.exe通过cmd触发，会被系统拦截

![](https://github.com/zhaoxinyuan996/auto-shutdown-py/blob/main/md/step1.png)

![](https://github.com/zhaoxinyuan996/auto-shutdown-py/blob/main/md/step2.png)

![](https://github.com/zhaoxinyuan996/auto-shutdown-py/blob/main/md/step3.png)

![](https://github.com/zhaoxinyuan996/auto-shutdown-py/blob/main/md/step4.png)

![](https://github.com/zhaoxinyuan996/auto-shutdown-py/blob/main/md/step5.png)

### 打包过程

源码用pyinstaller打包，具体需要的第三方包在hook-ctypes.macholib.py

自己打包最好使用虚拟环境，使exe文件体积最小化

## ui节点层级关系

```
{
  "base(根节点)": {
    "ta1(动作选项卡)": {
      "ta1(关机)": {},
      "ta2(重启)": {},
      "ta3(睡眠)": {},
      "ta4(休眠)": {},
      "ta5(局域网)": {},
      "ta6(自定义)": {}
    },
    "ta2(触发选项卡)": {
      "ta1(倒计时)": {
        "la1-la5": "文本",
        "te1-te4": "输入框"
      },
      "ta2(定时)": {
        "ti1-ti7": "复选框",
        "te1-te7": "输入框"
      },
      "ta3(自定义)": {}
    },
    "entry(条目栏)": [
      {
        "label": "文本",
        "name": "任务名称",
        "is_enable": "复选框",
        "btn": "删除按钮"
      }
    ] 
  }
}
```
