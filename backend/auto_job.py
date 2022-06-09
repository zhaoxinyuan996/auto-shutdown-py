import os
import sys
import json
import multiprocessing
from time import sleep
from file_opt import File
from datetime import datetime
from pydantic import BaseModel, validator
from typing import Dict, Union, List, Any, Tuple, Callable
from apscheduler.schedulers.background import BackgroundScheduler

# BackgroundScheduler
# BlockingScheduler
# 目前是用异步执行器


def wrap(func: Callable):
    """记录日志的装饰器"""
    def f(*args, **kwargs):
        with File('log', encoding='utf-8', mode='a') as file:
            file.write(f'{datetime.now()}-{func.__name__}-{args}-{kwargs}\n')
        return func(*args, **kwargs)
    return f


@wrap
def act_1():
    os.system('shutdown -f -s -t 0')


@wrap
def act_2():
    os.system('shutdown -r -f -t 0')


@wrap
def act_3(**kwargs):
    name = kwargs['name']
    repeat = kwargs['repeat']
    if repeat:
        os.popen(File.get_remind(name))
    else:
        os.system(File.get_remind(name))


@wrap
def act_3(**kwargs):
    os.system(kwargs['cmd'])


func_map = {
    '关机': act_1,
    '重启': act_2,
    '提醒': act_3,
    '命令': act_4
}


# =============入参结构=============
class BaseTri(BaseModel):
    trigger: str


class CdTri(BaseTri):
    run_date: datetime


class IntervalTri(BaseTri):
    seconds: int


class TimTri(BaseTri):
    year: Any
    month: Any
    day_of_week: Any
    day: Any
    hour: Any
    minute: Any
    second: Any


class Config(BaseModel):
    act: Tuple[str, dict]
    fac: Tuple[str, Union[CdTri, IntervalTri, TimTri]]
    name: str
    is_enable: bool
    _ = validator('act')(lambda t: (func_map[t[0]], t[1]))
# =============入参结构=============


class GetJob:
    # __class__伪单例，写在类命令空间即可
    def __init__(self): ...

    exec_list = []
    scheduler = BackgroundScheduler()

    with File('conf', encoding='utf-8') as f:
        config: List[Dict[str, Any]] = json.loads(f.read())

    def gen_params(self):
        """生成调度器的入参"""
        for i in self.config:
            if not i['is_enable']:
                continue

            conf = Config(**i).dict()
            kw = conf['fac'][1]
            func, kw['kwargs'] = conf['act']

            self.scheduler.add_job(func, **kw)

        self.scheduler.start()
        while 1:
            sleep(9999)


if __name__ == '__main__':
    # 可重入，杀掉原进程，重新生成一个定时进程
    main_name = os.path.basename(sys.argv[0])
    pid = multiprocessing.current_process().pid
    os.system(f'taskkill /f /fi "imagename eq {main_name}" /fi "pid ne {pid}"')
    # 启用调度器
    job = GetJob()
    job.gen_params()
