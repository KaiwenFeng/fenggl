def bubbesort(arr):
    x=len(arr)
    for i in range(x):
        for j in range(x-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

user_input = input("Enter numbers sparatd by a comma:").strip()
unsort =  [int(item) for item in user_input.split(',')] 
import time
start = time.process_time()
print(bubbesort(unsort))
print(f'Processing time: {time.process_time()-start}')

