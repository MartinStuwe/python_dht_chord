def hash_4bit(key):
    hash_value = hash(key)
    hash_4bit = hash_value % (2**4)

    return hash_4bit


class node:
    def __init__(self, id):
        self.hash = hash_4bit(id)
        self.pred = None
        self.succ = None
        self.data = []

class chord_dht:
    def __init__(self,ids, data):
        self.nodes = [node(id) for id in ids]
        self.data = data
        for i, nodei in enumerate(self.nodes):
            if(i < len(self.nodes) - 1):
                print(i)
                nodei.succ = self.nodes[i + 1]
                if(i == 0):
                    nodei.pred = self.nodes[-1]
                else:
                    nodei.pred = self.nodes[i - 1]

            if(i == len(self.nodes) - 1):
                nodei.succ = self.nodes[0]
                nodei.pred = self.nodes[i - 1]

        for i, nodei in enumerate(self.nodes):
            for j, dataj in enumerate(self.data):
                if nodei.pred.hash < nodei.hash:
                    if (dataj <= nodei.hash and dataj > nodei.pred.hash):
                        nodei.data.append(dataj) 
                else:
                    if (dataj <= nodei.hash or dataj > nodei.pred.hash):
                        nodei.data.append(dataj)


data = [0, 2, 3, 5, 6, 8, 9, 10, 11, 13, 15]
hashed_data = [hash_4bit(data) for _, data in enumerate(data)]
chord = chord_dht([1, 4, 7, 12, 14], hashed_data)

print([node.hash for node in chord.nodes])
print([node.data for node in chord.nodes])
print(hashed_data)


print(1 + ((2*3) % (2 ** 4)))