from reactivex import Observable
 
# Create an observable sequence
observable = Observable.from_iterable(range(5))
 
# Use operators to transform the sequence
transformed = observable.map(lambda x: x * 2).filter(lambda x: x > 5)
 
# Subscribe to the transformed sequence
transformed.subscribe(lambda x: print(f"Transformed Value: {x}"))
