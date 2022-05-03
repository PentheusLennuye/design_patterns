'''
File: design_patterns/observer/interfaces.py
'''

class Observer:
    '''Interface Observer that is registered with a Subject'''
    def update():
        '''This might be done better with another pattern. This remains with
           the three arguments for now to keep the OBSERVER demo simple.'''
        raise NotImplementedError


class Subject:
    '''Notifies its list of Observers on state change'''
    def register_observer(observer: Observer):
        raise NotImplementedError

    def remove_observer(observer: Observer):
        raise NotImplementedError

    def notify_observer():
        raise NotImplementedError


class DisplayElement:
    '''Used merely as a demonstration'''
    def display():
        raise NotImplementedError
