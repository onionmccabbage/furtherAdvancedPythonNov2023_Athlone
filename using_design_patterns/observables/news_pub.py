class NewPublisher():
    def __init__(self):
        '''publish a stream of events e.g. news stories, commentary, logs,keystrokes, data packets'''
        self.__subscribers = [] # begin with an empty list for our subscribers
        self.latest_news = None
    # Observables expose 'attach' and 'detach' methods for the subscribers
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # just remove the most recent subscriber
    def iter_subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    def notify_sub(self):
        for sub in self.__subscribers:
            sub.update() # call the update method of hte subscriber