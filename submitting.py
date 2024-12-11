import math
import matplotlib.pyplot as plt
class cache_builder():
    def __init__(self):
        self.cache = {}
        self.index_generator = []
        self.byte_offset = 0
        self.number_of_cache_lines = 0
        self.number_of_index_bits = 0
        self.number_of_tag_bits = 0
        self.ways = 0
        self.block_size = 0
        self.totol_size = 0
    
    def details(self, ways, block_size, totol_size):
        self.byte_offset = int(math.log(block_size, 2))
        self.number_of_cache_lines = int(totol_size / (block_size * ways))
        self.number_of_index_bits = int(math.log(self.number_of_cache_lines, 2))
        self.number_of_tag_bits = 32 - self.byte_offset - self.number_of_index_bits
        self.ways = ways
        self.block_size = block_size
        self.totol_size = totol_size
    
    def build_cache(self):
        for i in range(self.number_of_cache_lines):
            binary = bin(i)[2:].zfill(self.number_of_index_bits)
            self.index_generator.append(binary)
        
        for index in self.index_generator:
            self.cache[index] = myset(index, self.ways)
        
        for index in self.index_generator:
            self.cache[index].setup_set()

class myset():
    def __init__(self, index, ways):
        self.index = index
        self.ways = ways
        self.set = []
        self.lru_queue = []
    
    def setup_set(self):
        for i in range(self.ways):
            self.set.append([0, None])
            self.lru_queue.append(i)  

class cache_operator():
    def __init__(self, cache_builder):
        self.cache_builder = cache_builder
        self.memory_location = ""
        self.index = ""
        self.accessed_way = 0
        self.hit = 0
        self.miss = 0
        self.count = 0
    
    def priority(self, hit):
        if hit == 0:
            self.cache_builder.cache[self.index].lru_queue.append(self.accessed_way)
            self.cache_builder.cache[self.index].lru_queue.pop(0)
        elif hit == 1:
            if self.accessed_way in self.cache_builder.cache[self.index].lru_queue:
                self.cache_builder.cache[self.index].lru_queue.remove(self.accessed_way)
                self.cache_builder.cache[self.index].lru_queue.append(self.accessed_way)
        elif hit == 2:
            self.cache_builder.cache[self.index].lru_queue.pop(0)
            self.cache_builder.cache[self.index].lru_queue.append(self.accessed_way)

    def read(self, file_name):
        with open(file_name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                
                H = line.split()
                memory_location = H[1][2:]
                heaxadecimal_mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                                        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                                        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
                                        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
                temp = ''.join(heaxadecimal_mapping[ch] for ch in memory_location)
                self.memory_location = temp
                self.write()
        
        #print("HITS:", self.hit)
        #print("MISSES:", self.miss)
        #print("TOTAL ACCESSES:", self.count)
        return self.hit, self.miss

    def write(self):
        hit = 0
        self.index = self.memory_location[self.cache_builder.number_of_tag_bits:self.cache_builder.number_of_tag_bits + self.cache_builder.number_of_index_bits]
        self.tag_bits = self.memory_location[:self.cache_builder.number_of_tag_bits]
        cache_set = self.cache_builder.cache[self.index].set
        
        for i in range(self.cache_builder.ways):
            if cache_set[i][0] == 1 and cache_set[i][1] == self.tag_bits:
                self.accessed_way = i
                hit = 1
                self.priority(hit)
                self.hit += 1
                self.count += 1
                return
        
        for i in range(self.cache_builder.ways):
            if cache_set[i][0] == 0:
                self.accessed_way = i
                cache_set[i][0] = 1
                cache_set[i][1] = self.tag_bits
                self.priority(hit)
                self.miss += 1
                self.count += 1
                return
        
        hit = 2
        lru_way = self.cache_builder.cache[self.index].lru_queue[0]
        self.accessed_way = lru_way
        cache_set[lru_way][1] = self.tag_bits
        self.priority(hit)
        self.miss += 1
        self.count += 1

block_size = 4
ways=4
totol_size = 1024 * 1024
trace_files = ["gcc.trace","gzip.trace", "mcf.trace", "swim.trace", "twolf.trace"]
plt.figure()
for trace in trace_files:
    #print(trace)
    x = []
    y = []
    block_size = 1
    while block_size < 256:
        cache = cache_builder()
        cache.details(ways, block_size, totol_size)
        cache.build_cache()
        operator = cache_operator(cache)
        hit, miss = operator.read(trace)
        miss_rate = (miss / (miss + hit))*100
        x.append(block_size)
        y.append(miss_rate)
        block_size=block_size*2
    plt.plot(x, y,label=f'{trace}')
plt.ylabel('Miss_Rate')
plt.xlabel('Block_size')
plt.legend(loc="upper right")
plt.title('Miss_Rate vs Block_size')
plt.figure()
for trace in trace_files:
    #print(trace)
    x = []
    y = []
    block_size=4
    totol_size = 128
    while totol_size < 4096:
        cache = cache_builder()
        cache.details(ways, block_size, totol_size*1024)
        cache.build_cache()
        operator = cache_operator(cache)
        hit, miss = operator.read(trace)
        miss_rate = (miss / (miss + hit))*100
        x.append(totol_size)
        y.append(miss_rate)
        totol_size=totol_size*2
    plt.plot(x, y,label=f'{trace}')
    #print(x)
    #print(y)
plt.xlabel('Total_size')
plt.ylabel('Miss_rate')
plt.legend(loc="upper right")
plt.title('Miss_Rate vs Total_size')
plt.figure()
for trace in trace_files:
    #print(trace)
    x = []
    y = []
    block_size=4
    ways=1
    totol_size=1024
    while ways < 256:
        cache = cache_builder()
        cache.details(ways, block_size, totol_size*1024)
        cache.build_cache()
        operator = cache_operator(cache)
        hit, miss = operator.read(trace)
        hit_rate = (hit / (miss + hit))*100
        x.append(ways)
        y.append(hit_rate)
        ways=ways*2
    plt.plot(x, y,label=f'{trace}')
    #print(x)
    #print(y)
plt.xlabel('ways')
plt.ylabel('Hit_rate')
plt.legend(loc="upper right")
plt.title('hit_rate vs ways')
plt.show()

