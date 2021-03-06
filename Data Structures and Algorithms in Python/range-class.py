class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:    # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0, n)
        
        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)
        
        self._start = start 
        self._step = step 
    
    def __len__(self):
        return self._length
    def __getitem__(self, k):
        if k<0:             # attempt to convert negative index
            k+=len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step

for i in Range(6):
    print(i, end=" ")
for i in Range(-4, 6, 2):
    print(i, end=" ")
        
