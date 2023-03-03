#Import random digunakan untuk menghasilkan angka acak di pyhton
import random

#Kode bagian Shell sort
def ShellSort(data):
    gap = (len(data)//2)
    a=0
    while gap > 0 :
        for i in range(gap,len(data)):
            nilai = data[i]
            j = i

            while j >= gap and data[j-gap] > nilai:
                data[j] = data[j-gap]
                j-=gap

            data[j] = nilai
            print(data)
        print("Iterasi ke",a,": ",data,"dengan gap ",gap )
        a+=1

        gap //= 2

    return data
 #Kode bagian quick sort
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]

        greater = [x for x in arr[1:] if x > pivot]
    
    return QuickSort(less) + [pivot] + QuickSort(greater)


list = []

#Bagian Shell Sort
for i in range(15):
    list.append(random.randint(1, 100)) #memiliki fungsi untuk memanggil angka random dari 1-100
print("List Awal sebelum di shell sort:")
print(list)
print()

list = ShellSort(list)
print("\nList setelah diurutkan :")
print(list)
print()

#Bagian Quick Sort
for i in range(15):
    list.append(random.randint(1, 100))
print("List Awal sebelum di quick sort:")
print(list)
print()

list = QuickSort(list)
print("\nList setelah diurutkan :")
print(list)
print()