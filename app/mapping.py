from app.script import cd_check, timing_check, cmd_check, remind_check, interval_check

# Dict[选项卡名字: (取值, 校验)]
# 规范：如果校验函数是None，则直接跳过
add_map = {
    '关机': (None, None),
    '重启': (None, None),
    '提醒': ('self.base.ta1.ta3', remind_check),
    '命令': ('self.base.ta1.ta5.li1', cmd_check),

    '倒计时': ('self.base.ta2.ta1.time', cd_check),
    '间隔': ('self.base.ta2.ta2', interval_check),
    '定时': ('self.base.ta2.ta3', timing_check)
}

delete_map = {

}

save_map = {

}
