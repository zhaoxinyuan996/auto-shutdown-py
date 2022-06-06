import os
import json
from functools import partial
from script import ExtendJson
from qt.base_qt import BaseQt
from mapping import act_map, fac_map
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QPushButton, QMessageBox, QLineEdit


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
        name.setText(f'''{conf['act'][0]}->{conf['fac'][0]}''')

        # 重复功能貌似没意义
        # repeat = BaseQt(QCheckBox, e, name='repeat')
        # repeat.setGeometry(650, 0, 150, 50)
        # repeat.setChecked(True)
        # repeat.setText('重复')

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
            # repeat.setChecked(conf['repeat'])
            is_enable.setChecked(conf['is_enable'])

        e.show()
        # 配置
        e.conf = conf
        self.entry_list.append(e)

    def _check(self, _value, _map, _name):
        """上下选项卡相同逻辑，eval会用到self"""
        # 不飘黄行不行？
        _msg = self and {}
        if _value:
            _value = eval(_value)
            _msg = _map[_name][1](_value)
        return _msg

    @staticmethod
    def _get_act_fac(act_name, fac_name):
        act_value, act_check = act_map.get(act_name, (None, None))
        fac_value, fac_check = fac_map.get(fac_name, (None, None))

        err = ''
        if act_value is None:
            err += f'动作[{act_name}]未实现\n'
        if fac_value is None:
            err += f'触发[{fac_name}]未实现\n'
        if err:
            raise ValueError(err)

        return act_value, act_check, fac_value, fac_check

    def check(self):
        """检查当前入参，失败返回false，成功返回配置"""
        # entry总体检查
        if self.length >= 5:
            return ValueError('只能存在5条任务')
        # entry内容检查
        try:
            act_name = self.base.ta1.tabText(self.base.ta1.currentIndex())
            fac_name = self.base.ta2.tabText(self.base.ta2.currentIndex())
            act_value, act_check, fac_value, fac_check = self._get_act_fac(act_name, fac_name)
            # 有值则校验
            act_msg = self._check(act_value, act_map, act_name)
            fac_msg = self._check(fac_value, fac_map, fac_name)
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
            # i.conf['repeat'] = bool(i.repeat.checkState())
            config.append(i.conf)
        with open('./config.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(config, ensure_ascii=False, cls=ExtendJson))

        print(config)
        self.activate_job()
        QMessageBox.critical(self.base, '应用', '应用成功')

    def recovery(self):
        """读取配置文件恢复ui"""
        with open('./config.json', encoding='utf-8') as f:
            config = json.loads(f.read())
        for i in config:
            self.add_entry(i)

    @staticmethod
    def activate_job():
        """触发后台任务"""
        print(os.system(r'.\auto_job.exe'))
