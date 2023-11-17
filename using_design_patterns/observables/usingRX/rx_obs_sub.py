# pip install rx
from reactivex import create

# def push(observer, scheduler):
#     observer.on_next('test 1 pass')
#     observer.on_next('test 2 pass')
#     observer.on_next('test 2 fail')
#     observer.on_next('test 4 pass')
#     observer.on_next('test 5 fail')

# source = create(push)

# source.subscribe(
#     on_next = lambda i:print(f'Received {i}'),
#     on_error = lambda e: print(f'Error {e}'),
#     on_completed = lambda: print('All done')
# )

from reactivex import of
# source may be ANY stream of data 
source = of('t1', 't2', 't3', 't4', 't5')
source.subscribe(
    on_next = lambda i:print(f'Received {i}'),
    on_error = lambda e: print(f'Error {e}'),
    on_completed = lambda: print('All done')
)
source.subscribe(
    on_next = lambda i:print(f'Handled {i}'),
    on_error = lambda e: print(f'Error {e}'),
    on_completed = lambda: print('All done')
)
