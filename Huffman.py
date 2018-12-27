
class minheap(object):
    
    def __init__(self):
        #super(minheap, self).__init__()
        self.array = [];
        self.current_size = 0;

    def shift_up(self,i):
        while i//2 > 0:
            if self.array[i] < self.array[i//2]:
                self.array[i] , self.array[i//2] =self.array[i//2] , self.array[i]
            i = i//2

    def shift_down(self,i):
        
        while (i * 2) <= self.current_size:
            
            
            if i * 2 + 1 > self.current_size:
                
                if self.array[i]> self.array[2*i]:
                    self.array[2*i], self.array[i] = self.array[i], self.array[2*i]
                i = 2*i    
            elif self.array[i]> min(self.array[2*i],self.array[2*i+1]):
               
                if self.array[2*i] < self.array[2*i+1]:
                    
                    self.array[2*i], self.array[i] = self.array[i], self.array[2*i]
                    i = i* 2
                    
                    
                else:
                    
                    self.array[2*i+1], self.array[i] = self.array[i], self.array[2*i+1]
                    i = 2*i +1
            else:
                break
        

    def pop(self):
            
            if(self.current_size>0):
                last = self.array[self.current_size]
                min_val = self.array[1]
                self.array[1] = last
                self.current_size -=1
                self.array.pop()
                self.shift_down(1)
                return min_val
    def push(self,k):
            self.array.append(k)
            self.current_size = self.current_size + 1
            self.shift_up(self.current_size)


    def heapify(self,lst):
        self.array = [0]+lst
        self.current_size = len(lst)
        i = self.current_size//2
        while i > 0 :
           
            self.shift_down(i)
            i -=1

def huffman(frequency):
    huff_heap=minheap()
    lst = [[wt, [sym, ""]] for sym, wt in frequency.items()]
    huff_heap.heapify(lst)
    
    while len(huff_heap.array) > 2:
        left = huff_heap.pop()
        right = huff_heap.pop()
        
        for freq in left[1:]:
            freq[1] = '0' + freq[1]
        for freq in right[1:]:
            freq[1] = '1' + freq[1]
            
        huff_heap.push( [left[0] + right[0]] + left[1:] + right[1:])
    ans = []

    ans = huff_heap.array[1][1:]
    
    return sorted(ans, key=lambda x: len(x[1]))

frequency = input ("give frequency dictionary")



huff_list = huffman(frequency)

print "Symbol\tWeight\tHuffman Code"
for t in huff_list:
    print "%s\t%s\t%s" % (t[0], frequency[t[0]], t[1])

