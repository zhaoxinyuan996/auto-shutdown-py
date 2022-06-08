from json import JSONEncoder
from datetime import datetime
from time import time, strftime, localtime


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


def timing_check(v):
    """定时校验，按照定时库的参数，v: self.base.ta2.ta2"""
    conf = {}
    for i, kv in enumerate(cron_check.items()):
        label = getattr(v, f'te{i + 1}').text()
        # 勾选就是*
        if getattr(v, f'ti{i + 1}').checkState():
            conf[kv[0]] = '*'
            continue
        # 不勾选就校验是否合法，主要是防止定时器库报错
        if label:
            label = int(label)
            start, end = kv[1]
            if start <= label <= end:
                conf[kv[0]] = label
            else:
                raise ValueError(f'{shadow_flag[i]}的范围要在{start}和{end}之间')
    if not conf:
        raise ValueError('至少选1个')

    return {'trigger': "cron", **conf}


# ============各种类型的校验============
