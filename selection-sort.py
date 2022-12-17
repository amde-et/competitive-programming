class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min=arr[i]
            tmp=i
            for j in range(i+1,n):
               if arr[j]<min:
                   min=arr[j]
                   tmp=j
            arr[i],arr[tmp]=arr[tmp],arr[i]
