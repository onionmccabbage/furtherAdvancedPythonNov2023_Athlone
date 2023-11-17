from reactivex import Observable, of
 
# Create an observable sequence
observable = of(*range(5)) # * will unpack the values
 

# Subscribe to the transformed sequence
observable.subscribe(lambda x: print(f"observed Value: {x}"))
