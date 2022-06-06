from script import cd_check, timing_check

# Dict[选项卡名字: (取值, 校验)]
act_map = {
    '关机': ('', None),
}

fac_map = {
    '倒计时': ('self.base.ta2.ta1.time', cd_check),
    '定时': ('self.base.ta2.ta2', timing_check),
    '自定义': ''
}

backend_map = {
    '关机': 'shutdown now'
}
