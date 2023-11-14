from news_pub import NewPublisher
from email_sub import EmailSubscriber
from print_sub import PrintSubscriber
from media_sub import MediaSubscriber

subs_t = (EmailSubscriber, PrintSubscriber, MediaSubscriber)

def main():
    '''invoke the publisher and subscribers'''
    news_pub = NewPublisher()
    for sub in subs_t:
        sub(news_pub)
        news_pub.add_news('New Flash - it will soon be lunch!!')
    news_pub.notify_sub() # they all get notified of this news

if __name__ == '__main__':
    main()