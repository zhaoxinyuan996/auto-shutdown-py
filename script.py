from time import time, strftime, localtime


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
# ============各种类型的校验============
def cd_check(v):
    """倒计时校验，v: self.base.ta2.ta1.time"""
    if not v:
        raise ValueError('倒计时不可为0')
    return v


lis = ['year', 'mon', 'w_day', 'day', 'hour', 'min', 'sec']


def timing_check(v):
    """定时校验，v: self.base.ta2.ta2"""
    conf = {}
    for i, t in enumerate(lis):
        label = getattr(v, f'te{i + 1}').text()
        tmp = 0 if getattr(v, f'ti{i + 1}').checkState() else (int(label) if label else None)
        if tmp is not None:
            conf[t] = tmp

    return conf


# ============各种类型的校验============
