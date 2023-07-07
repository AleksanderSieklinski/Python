#Proszę zaimplementować funkcje generatorowe wykonujące sortowanie elementów listy stosując sortowanie bąbelkowe oraz sortowanie przez scalanie (plik alg_sort.pdf). 
#Proszę utworzyć animację, równocześnie obrazującą sortowanie obiema metodami, listy zawierającej 50 całkowitych wartości losowych.

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            yield arr
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def mergeSort(arr, start, end):
    if end <= start:
        return
    mid = start + ((end-start+1)//2)
    yield from mergeSort(arr, start, mid-1)
    yield from mergeSort(arr, mid, end)
    yield from merge(arr, start, mid-1, end)


def merge(arr, start, mid, end):
    result = []
    left_index = start
    right_index = mid + 1
    while left_index <= mid and right_index <= end:
        if arr[left_index] < arr[right_index]:
            result.append(arr[left_index])
            left_index+=1
        else:
            result.append(arr[right_index])
            right_index+=1
   
    while left_index <= mid:
        result.append(arr[left_index])
        left_index+=1
   
    while right_index <= end:
        result.append(arr[right_index])
        right_index+=1
   
    for index, value in enumerate(result):
        arr[start+index] = value
        yield arr

            
def animate(arr):

    def update_plot1(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        return bars

    def update_plot2(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        return bars
    
    bubble = bubbleSort(arr.copy())
    merge = mergeSort(arr.copy(),0,len(arr)-1)
    fig, (ax1,ax2) = plt.subplots(1,2)
    ax1.set_title("Bubble sort")
    ax2.set_title("Merge sort")
    ax1.set_xlim(0, N)
    ax1.set_ylim(0, 100)
    ax2.set_xlim(0, N)
    ax2.set_ylim(0,100)
    bars1 = ax1.bar(range(len(arr)), arr[:], align="edge")
    anim1 = FuncAnimation(fig, func=update_plot1, fargs=(bars1,), frames=bubble, interval=1, repeat=False)
    bars2 = ax2.bar(range(len(arr)), arr[:], align="edge")
    anim2 = FuncAnimation(fig, func=update_plot2, fargs=(bars2,), frames=merge, interval=1, repeat=False)
    plt.show()

if __name__ == "__main__":
    N = 50
    arr = [random.randint(1, 100) for _ in range(N)]        
    animate(arr)
