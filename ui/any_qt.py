from functools import partial
import json
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QMessageBox, QLineEdit

from mapping import act_map, fac_map
from ui.base_qt import BaseQt


class Entry:
    """明细条目类"""
    def __init__(self, base):
        self.base = base
        self.entry_list = []

        # 限制只能有5个待办条目
        self.length = 0

    def build_entry(self, conf, from_file=False):
        """嵌套结构的条目"""
        # ui
        e = BaseQt(QWidget, self.base)
        e.setGeometry(0, self.base.size_shadow[1], 1000, 50)

        label = BaseQt(QLabel, e, name='label')
        label.setGeometry(0, 0, 100, 50)
        label.setText('任务名称')

        name = BaseQt(QLineEdit, e, name='name')
        name.setGeometry(100, 0, 500, 50)

        repeat = BaseQt(QCheckBox, e, name='repeat')
        repeat.setGeometry(650, 0, 150, 50)
        repeat.setChecked(True)
        repeat.setText('重复')

        is_enable = BaseQt(QCheckBox, e, name='is_enable')
        is_enable.setGeometry(780, 0, 150, 50)
        is_enable.setChecked(True)
        is_enable.setText('启用')

        btn = BaseQt(QPushButton, e, name='btn')
        btn.clicked.connect(partial(self.del_entry, e))
        btn.setGeometry(900, 0, 100, 50)
        btn.setText('删除')

        if from_file:
            name.setText(conf['name'])
            repeat.setChecked(conf['repeat'])
            is_enable.setChecked(conf['is_enable'])

        e.show()
        # 配置
        e.conf = conf
        self.entry_list.append(e)

    def check(self):
        """检查当前入参，失败返回false，成功返回配置"""
        # entry总体检查
        if self.length >= 5:
            return ValueError('只能存在5条任务')
        # entry内容检查
        act_msg = fac_msg = None
        act_name = self.base.ta1.tabText(self.base.ta1.currentIndex())
        fac_name = self.base.ta2.tabText(self.base.ta2.currentIndex())
        act_value, act_check = act_map[act_name]
        fac_value, fac_check = fac_map[fac_name]
        # 有值则校验
        if act_value:  # 上部选项卡参数校验
            act_value = eval(act_value)
            try:
                act_msg = fac_map[act_name][1](act_value)
            except ValueError as e:
                return e
        if fac_value:  # 下部选项卡参数校验
            fac_value = eval(fac_value)
            try:
                fac_msg = fac_map[fac_name][1](fac_value)
            except ValueError as e:
                return e

        return {
                'act': (act_name, act_msg),
                'fac': (fac_name, fac_msg)
                }

    def add_entry(self, from_file):
        """添加条目总入口"""
        if from_file:  # 如果是从文件恢复，不做任何check，直接添加
            msg = from_file
            self.build_entry(msg, from_file=True)

        else:   # 如果是手动添加，需要检查
            msg = self.check()
            if isinstance(msg, Exception):
                QMessageBox.critical(self.base, '错误', str(msg))
                return
            else:
                self.build_entry(msg)
        # 主界面回调
        self.base.size_shadow[1] += 50
        self.base.resize(*self.base.size_shadow)
        self.length += 1

    def del_entry(self, e):
        """删除条目"""
        self.entry_list.remove(e)
        e.deleteLater()
        self.base.size_shadow[1] -= 50
        self.base.resize(*self.base.size_shadow)
        self.length -= 1
        # 重新排列，这里限制5条，不考虑list时间复杂度问题
        for i, e in enumerate(self.entry_list):
            e.move(0, 850 + 50 * (i - 1))

    def save(self):
        """保存到配置文件"""
        config = []
        for i in self.entry_list:
            i.conf['name'] = i.name.text()
            i.conf['is_enable'] = bool(i.is_enable.checkState())
            i.conf['repeat'] = bool(i.repeat.checkState())
            config.append(i.conf)
        with open('./config.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(config, ensure_ascii=False))

        print(config)
        self.activate_job()

    def recovery(self):
        """读取配置文件恢复ui"""
        with open('./config.json', encoding='utf-8') as f:
            config = json.loads(f.read())
        for i in config:
            self.add_entry(i)

    def activate_job(self):
        """触发后台任务"""
        ...


def ta2_ta2_tick_click(tick_no, self):
    """复选框联动文本框，self: base.ta2.ta2"""
    label = getattr(self, f'te{tick_no}')
    flag = getattr(self, f'ti{tick_no}').checkState()
    label.setEnabled(not flag)
