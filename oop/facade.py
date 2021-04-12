
# from datetime import datetime
import time
import random 
# from vigilance import _Vigilance
# from awake import _Awake
# from work import _Work
# from caffeine import _Caffeine
# from sickness import _Sickness
# from _time import _Time


class _Awake(object):

    is_awake = False

    @staticmethod
    def get(now):

        if 5 < now < 22:
            return True

        return False


class _Vigilance(object):

    def __init__(self, lvl = 100):

        self._lvl = lvl

    @property
    def lvl(self):

        return self._lvl
    
    @lvl.setter
    def lvl(self, lvl):

        self._lvl = lvl


class _Time(object):

    bed = 22
    now = 6

    def do_time(self):

        self.now += 1


class _Sickness(object):

    @staticmethod
    def is_sick_day():

        chance = random.randrange(0, 100)
        if chance > 90:
            return True

        return False


class _Caffeine(object):

    lvl = 0
    max_lvl = 50

    def increase(self, vigilance):

        if self.lvl <= self.max_lvl:
            self.lvl += 15
            vigilance += 40
        
        return vigilance


class _Work(object):

    def do_work(self):

        self.time.now += 1
        self.vigilance._lvl -= 10
        print('Working, Time: {}'.format(self.time.now))
        self.is_issue_raised()

    def is_issue_raised(self):

        if self.time.now % 2:
            print('Issue raised, Time: {}'.format(self.time.now))
            self.vigilance._lvl -= 25

    @staticmethod
    def critical_issue():

        chance = random.randrange(0, 100)
        if chance > 70:
            return True

        return False


# Facade.
class Programmer(_Work):

    def __init__(self):

        self.awake = _Awake()
        self.vigilance = _Vigilance()
        self.time = _Time()
        self.sickness = _Sickness()
        self.caffeine = _Caffeine()
        
    def start(self):

        if self.critical_issue() or \
            self.awake.get(self.time.now) or\
            not self.sickness.is_sick_day():
                self.awake.is_awake = True
                return True

        if not self.awake.get(self.time.now):
            print('Nerd not ready.')
            
        if self.sickness.is_sick_day():
            print('Nerd is sick.')
  
        return False

    def wake_up(self):

        time.sleep(1)
        if self.time.now < 8:

            self.time.do_time()
            print('Waking up..., Time: {}'.format(self.time.now))
            return self.wake_up()
            
        else: 
            print('Wakeup finished, Time: {}'.format(self.time.now))
            return True

    def work_done(self):
        
        time.sleep(1)
        if self.time.now < 16 and self.vigilance._lvl > 20:
            self.do_work()
            if self.vigilance._lvl <= 50:
                self.vigilance._lvl = self.caffeine.increase(self.vigilance._lvl)
                print('Coffee loaded.')

            return self.work_done()

        else:
            print('Work done, Time: {}'.format(self.time.now))
            return True


if __name__ == "__main__":
    
    nerd = Programmer()
    if nerd.start():
        if nerd.wake_up():
            if nerd.work_done():
                print('Work done.')