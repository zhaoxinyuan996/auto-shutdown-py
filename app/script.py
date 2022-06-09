import os
from typing import List
from hashlib import sha1
from file_opt import File
from json import JSONEncoder
from datetime import datetime
from time import time, strftime, localtime
from apscheduler.schedulers.background import BlockingScheduler


class ExtendJson(JSONEncoder):
    """pickle可读性较差，这里对于json额外做了下兼容，读取配置采用pydantic转换"""
    def default(self, o):
        if isinstance(o, datetime):
            return str(o)
        else:
            return super().default(o)


def cd_to_sec(self):
    """根据倒计时获取秒数并更新到label，self:base."""
    sec = \
        int(self.te1.text() or 0) * 86400 + \
        int(self.te2.text() or 0) * 3600 + \
        int(self.te3.text() or 0) * 60 + \
        int(self.te4.text() or 0)
    self.la3.setText(f'{sec}')
    self.time = int(time()) + sec  # 触发时间戳
    self.la5.setText(strftime("%Y-%m-%d %H:%M:%S", localtime(self.time)))


# 有返回则代表校验失败
# 简单且固定的校验就不引用pydantic了
# ============各种类型的校验============
def cd_check(v):
    """倒计时校验，v: self.base.ta2.ta1.time"""
    if not v:
        raise ValueError('倒计时不可为0')

    return {
        'trigger': "date",
        'run_date': datetime.fromtimestamp(v)
    }


shadow_flag = ['年', '月', '星期', '日', '时', '分', '秒']
cron_check = {
    'year': (2000, 9999),
    'month': (1, 12),
    'day_of_week': (0, 6),
    'day': (1, 31),
    'hour': (0, 23),
    'minute': (0, 59),
    'second': (0, 59)
}

# 这个校验太复杂了，交给库做吧
b = BlockingScheduler()


def timing_check(v):
    """定时校验，按照定时库的参数，v: self.base.ta2.ta2"""
    conf = {}
    for i, kv in enumerate(cron_check.items()):
        label = getattr(v, f'te{i + 1}').text()
        # 勾选就是*，
        if getattr(v, f'ti{i + 1}').checkState():
            conf[kv[0]] = '*'
        elif label:
            conf[kv[0]] = label

    if not conf:
        raise ValueError('至少选1个')
    # 这里值不合法会抛ValueError
    b.add_job(lambda: 0, trigger='cron', **conf)
    b.remove_all_jobs()

    return {'trigger': "cron", **conf}


def interval_check(v):
    """时间间隔check，v:v:self.base.ta2.ta2"""
    sec = int(v.li1.text() or 0)
    if sec == 0:
        raise ValueError('时间间隔必须大于0秒')
    return {'trigger': 'interval', 'seconds': sec}


def remind_check(v):
    """vbs脚本提示参数检查，v:self.base.ta1.ta3"""
    words: str = v.li1.text()
    repeat = bool(v.ti1.checkState())
    if not words:
        raise ValueError('请输入提示语！')
    # 判断文件是否存在
    timestamp = str(time())
    name = sha1(timestamp.encode()).hexdigest() + '.vbs'

    return {'name': name, 'repeat': repeat, 'msg': words}


def cmd_check(v):
    """包装一层cmd空check，原样返回，v:self.base.ta1.ta5.ti1"""
    return {'cmd': str(v.text())}

# ============各种类型的校验============


# ============保存hook============
def file_save_hook(v: List[dict]):
    """vbs脚本提示参数检查，v:conf"""
    # 目前只有remind文件夹，后期多了可以拆出去
    remind_dir = os.path.dirname(File.get_remind(''))
    files = set(os.listdir(remind_dir))
    shadow_files = set(files)
    for i in v:
        if i['act'][0] != '提醒':
            continue
        file_name = i['act'][1]['name']
        if file_name in files:
            shadow_files.remove(file_name)
        else:
            path = File.get_remind(file_name)
            with File(path, encoding='ansi', mode='w') as f:
                f.write(fr'''x=Msgbox("{i['act'][1]['msg']}",64,FormatDateTime(Now, vbLongDate))''')
    # 不在配置文件的都删除
    for i in shadow_files:
        os.remove(File.get_remind(i))
