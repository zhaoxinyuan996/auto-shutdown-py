import json
import multiprocessing
import sys
import os
from time import sleep
from datetime import datetime
from typing import Dict, Union, List, Any, Tuple, Callable
from pydantic import BaseModel, validator
from apscheduler.schedulers.background import BackgroundScheduler
# BackgroundScheduler
# BlockingScheduler
# 目前是用异步执行器


def wrap(func: Callable):
    """记录日志的装饰器"""
    def f(*args, **kwargs):
        with open('logs', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()}-{func.__name__}-{args}-{kwargs}\n')
        return func(*args, **kwargs)
    return f


@wrap
def act_1():
    print('shutdown')


func_map = {
    '关机': act_1
}


# =============入参结构=============
class BaseTri(BaseModel):
    trigger: str


class CdTri(BaseTri):
    run_date: datetime


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
    fac: Tuple[str, Union[CdTri, TimTri]]
    name: str
    is_enable: bool
    _ = validator('act')(lambda t: (func_map[t[0]], t[1]))
# =============入参结构=============


class GetJob:
    # __class__伪单例，写在类命令空间即可
    exec_list = []
    scheduler = BackgroundScheduler()
    with open('../config.json', encoding='utf-8') as f:
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
    name = os.path.basename(sys.argv[0])
    pid = multiprocessing.current_process().pid
    os.system(f'taskkill /f /fi "imagename eq {name}" /fi "pid ne {pid}"')
    # 启用调度器
    job = GetJob()
    job.gen_params()
