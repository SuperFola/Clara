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


class TriggerEvent:
    def __init__(self, at: float):
        self.triggered = False
        self.time = at

    def trigger(self):
        """Activate the trigger"""
        self.triggered = True


class Action:
    def __init__(self, name: str=""):
        self.name = name


class Habit:
    def __init__(self, name: str, trigger_event: TriggerEvent, action: Action):
        self.name = name
        self.trigger_event = trigger_event
        self.launched = False
        self.action = action

    def check(self) -> object:
        """Check if the habit should be launched"""
        if self.trigger_event.triggered:
            self.start()
        return self

    def start(self) -> object:
        """Start 'doing' the habit"""
        self.launched = True
        return self

    def stop(self) -> object:
        """Stop 'doing' an habit"""
        self.launched = False
        return self


class Event(Habit):
    def __init__(self, name: str, trigger_event: TriggerEvent, action: Action):
        super().__init__(name, trigger_event, action)
        self.has_already_been_launched = False

    def start(self) -> object:
        """Start 'doing' the habit"""
        if not self.has_already_been_launched:
            self.has_already_been_launched = True
            super(self).start()