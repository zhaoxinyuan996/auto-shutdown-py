import json
from functools import partial
from app.qt.base_qt import BaseQt
from file_opt import File, call_file, call_func
from app.script import ExtendJson, file_save_hook
from app.mapping import add_map, delete_map, save_map
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
        e.setGeometry(0, self.base.size_shadow[1], 1000, 20)

        label = BaseQt(QLabel, e, name='label')
        label.setGeometry(5, 0, 100, 20)
        label.setText('任务名称')

        name = BaseQt(QLineEdit, e, name='name')
        name.setGeometry(60, 0, 250, 20)
        name.setText(f'''{conf['act'][0]}->{conf['fac'][0]}''')

        is_enable = BaseQt(QCheckBox, e, name='is_enable')
        is_enable.setGeometry(330, 0, 150, 20)
        is_enable.setChecked(True)
        is_enable.setText('启用')

        btn = BaseQt(QPushButton, e, name='btn')
        btn.clicked.connect(partial(self.del_entry, e))
        btn.setGeometry(400, 0, 100, 20)
        btn.setText('删除')

        if from_file:
            name.setText(conf['name'])
            is_enable.setChecked(conf['is_enable'])

        e.show()
        # 配置
        e.conf = conf
        self.entry_list.append(e)

    def _entry_hook(self, act_name, fac_name, method):
        """对应不同的hook函数，报错统一抛ValueError"""
        method = method or self
        map_ = {
            'add': add_map,
            'save': save_map,
            'delete': delete_map
        }[method]
        hook = map_.get(act_name)
        act_res = hook and hook[1] and hook[1](eval(hook[0]))
        hook = map_.get(fac_name)
        fac_res = hook and hook[1] and hook[1](eval(hook[0]))
        return act_res, fac_res

    def check(self):
        """检查当前入参，失败返回false，成功返回配置"""
        # entry总体检查
        if self.length >= 5:
            return ValueError('只能存在5条任务')
        # entry内容检查
        try:
            act_name = self.base.ta1.tabText(self.base.ta1.currentIndex())
            fac_name = self.base.ta2.tabText(self.base.ta2.currentIndex())
            err = ''
            err += '' if act_name in add_map else f'动作[{act_name}]未实现\n'
            err += '' if fac_name in add_map else f'动作[{fac_name}]未实现\n'
            if err:
                raise ValueError(err)
            act_msg, fac_msg = self._entry_hook(act_name, fac_name, 'add')

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
        self.base.size_shadow[1] += 20
        self.base.resize(*self.base.size_shadow)
        self.length += 1

    def del_entry(self, e):
        """删除条目"""
        # 删除hook
        try:
            self._entry_hook(e.conf['act'][0], e.conf['fac'][0], 'delete')
        except ValueError as e:
            QMessageBox.critical(self.base, '错误', str(e))
            return
        # 删除逻辑
        self.entry_list.remove(e)
        e.deleteLater()
        self.base.size_shadow[1] -= 20
        self.base.resize(*self.base.size_shadow)
        self.length -= 1
        # 重新排列，这里限制5条，不考虑list时间复杂度问题
        for i, e in enumerate(self.entry_list):
            e.move(0, 420 + 20 * (i - 1))

    def save(self):
        """保存到配置文件"""
        config = []
        for i in self.entry_list:
            i.conf['name'] = i.name.text()
            i.conf['is_enable'] = bool(i.is_enable.checkState())
            config.append(i.conf)
            # 保存hook
        file_save_hook(config)

        with File('conf', encoding='utf-8', mode='w') as f:
            f.write(json.dumps(config, ensure_ascii=False, cls=ExtendJson))
        print(config)
        self.activate_job()
        QMessageBox.about(self.base, '应用', '应用成功')

    def recovery(self):
        """读取配置文件恢复ui"""
        with File('conf', encoding='utf-8') as f:
            config = json.loads(f.read())
        for i in config:
            self.add_entry(i)

    @staticmethod
    def activate_job():
        """触发后台任务"""
        call_func(call_file)
