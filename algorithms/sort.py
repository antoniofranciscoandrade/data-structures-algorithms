import heapq

def selection_sort(array):
    for i in range(len(array)):
        min_val = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_val]:
                min_val = j
        temp = array[i]
        array[i] = array[min_val]
        array[min_val] = temp
    return array

def insertion_sort(array):
    for i in range(len(array)):
        pivot = i
        compare = i-1
        while compare >=0 and array[compare] > array[pivot]:
            temp = array[compare]
            array[compare] = array[pivot]
            array[pivot] = temp
            pivot -= 1
            compare -= 1
    return array

class HeapSort:
    def build_max_heap(self, array):
        for i in range(len(array)):
            parent = int((i-1)/2)
            while i > 0:
                if array[parent] < array[i]:
                    temp = array[i]
                    array[i] = array[parent]
                    array[parent] = temp
                    i = parent
                    parent = int((i-1)/2)
                else:
                    break
        return array
    
    def sink(self, array, heap_size):
        pos = 0
        while pos < int((heap_size-1)/2):
            left = 2*pos+1
            right = 2*pos+2
            if right >= heap_size:
                to_swap = left
            else:
                to_swap = left if array[left] > array[right] else right

            if array[to_swap] > array[pos]:
                temp = array[pos]
                array[pos] = array[to_swap]
                array[to_swap] = temp
                pos = to_swap
            else:
                break
        
        return array

    def sort(self, array):
        array = self.build_max_heap(array)
        for i in range(len(array)-1,-1,-1):
            temp = array[i]
            array[i] = array[0]
            array[0] = temp
            array = self.sink(array, i)        
        return array

class MergeSort:
    def merge(self, a1, a2):
        out = []
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(a1) and pointer2 < len(a2):
            if a1[pointer1] < a2[pointer2]:
                out.append(a1[pointer1])
                pointer1 += 1
            else:
                out.append(a2[pointer2])
                pointer2 += 1

        for _ in range(pointer1, len(a1)):
            out.append(a1[pointer1])
            pointer1 += 1

        for _ in range(pointer2, len(a2)):
            out.append(a2[pointer2])
            pointer2 += 1

        return out
    
    def ms(self, array):
        if len(array) == 1:
            return array

        mid = int(len(array)/2) 
        left = self.ms(array[:mid])
        right = self.ms(array[mid:])
        return self.merge(left, right)
        
    def sort(self, array):
        return self.ms(array)

class QuickSort:
    def partition(self, array, left, right):
        pivot = left
        while left <= right:
            while array[left] < array[pivot]:
                left+=1
            while array[right] > array[pivot]:
                right-=1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left +=1
                right-=1

        array[pivot], array[left-1] = array[left-1], array[pivot]
        return left-1
    
    def quick_sort(self, array, left, right):
        if left >= right:
            return
        pivot = self.partition(array, left, right)
        self.quick_sort(array, left, pivot-1)
        self.quick_sort(array, pivot+1, right)

    def sort(self, array):
        self.quick_sort(array, 0, len(array)-1)
        return array

