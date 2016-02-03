__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


class Time:
    def __init__(self):
        self.time = 0
        self.minute_lenght = 60
        self.hour_lenght = 60
        self.day_lenght = 24
        self.week_lenght = 7
        self.year_lenght = 52

    def next(self):
        """Update the current time"""
        self.time += 1

    def get_in_minutes(self) -> int:
        """Return the current time in minutes"""
        return self.time // self.minute_lenght

    def get_in_hours(self) -> int:
        """Return the current time in hours"""
        return self.get_in_minutes() // self.hour_lenght

    def get_in_days(self) -> int:
        """Return the current time in days"""
        return self.get_in_hours() // self.day_lenght

    def get_in_weeks(self) -> int:
        """Return the current time in weeks"""
        return self.get_in_days() // self.week_lenght

    def get_in_year(self) -> int:
        """Return the current time in years"""
        return self.get_in_weeks() // self.year_lenght

    def get_full_year_length_in(self, category: str) -> int:
        """Return the length of the year in 'category' unit"""
        if category.lower() in ['years', 'weeks', 'days', 'hours', 'minutes', 'seconds']:
            if category.lower() == 'years':
                return 1
            elif category.lower() == 'weeks':
                return self.year_lenght
            elif category.lower() == 'days':
                return self.week_lenght * self.get_full_year_length_in('weeks')
            elif category.lower() == 'hours':
                return self.day_lenght * self.get_full_year_length_in('days')
            elif category.lower() == 'minutes':
                return self.hour_lenght * self.get_full_year_length_in('hours')
            elif category.lower() == 'seconds':
                return self.minute_lenght * self.get_full_year_length_in('minutes')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.time)


class Condition:
    def __init__(self, key: str, value, importance: float):
        self.key = key
        self.value = value
        self.importance = importance


class TriggerEvent:
    def __init__(self, at: float, cond: list):
        self.triggered = False
        self.time = at
        self.condition = cond

    def check(self, current: list) -> bool:
        """Check if the trigger should be launched or not"""
        total = 0.0
        for state in current:
            for cond in self.condition:
                if state.key == cond.key and state.value == cond.value:
                    total += cond.importance
                if total >= 1.0:
                    break
            if total >= 1.0:
                break
        if total:
            self.trigger()
        else:
            self.untrigger()
        return self.triggered

    def should_last(self, states: list) -> bool:
        """Check if the trigger should stay on for a time or turn off"""
        for state in states:
            for cond in self.condition:
                if cond.key == "end_time" and state.key == "time" and cond.value == state.value:
                    return False
                elif cond.key == "end_time" and state.key == "time" and cond.value > state.value:
                    return True
        return False

    def untrigger(self):
        """Disable the trigger"""
        self.triggered = False

    def trigger(self):
        """Activate the trigger"""
        self.triggered = True


class Action:
    def __init__(self, name: str=""):
        self.name = name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Habit:
    def __init__(self, name: str, trigger_event: TriggerEvent, action: Action):
        self.name = name
        self.trigger_event = trigger_event
        self.launched = False
        self.action = action

    def check(self, states: list) -> bool:
        """Check if the habit should be launched"""
        self.trigger_event.check(states)
        if self.trigger_event.triggered and not self.launched:
            self.start()
        elif self.launched:
            if not self.trigger_event.should_last(states):
                self.stop()
        return self.launched

    def start(self) -> object:
        """Start 'doing' the habit"""
        self.launched = True
        return self

    def stop(self) -> object:
        """Stop 'doing' an habit"""
        self.launched = False
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Event(Habit):
    def __init__(self, name: str, trigger_event: TriggerEvent, action: Action):
        super().__init__(name, trigger_event, action)
        self.has_already_been_launched = False

    def start(self) -> object:
        """Start 'doing' the habit"""
        if not self.has_already_been_launched:
            self.has_already_been_launched = True
            self.launched = True
        return self