import heapq

class Node:
	def __init__(self,freq,char=None):
		self.freq=freq
		self.char = char
		self.left=None
		self.right= None


def huffman_tree(freq_dict):
	priority_q = [Node(freq,char) for char,freq in freq_dict.items()]
	heapq.heapify(priority_q)
	
	while len(priority_q)>1:
		left = heapq.heappop(priority_q)
		right = heapq.heappop(priority_q)
		
		combined = Node(left.freq+right.freq)
		combined.left = left
		combined.right = right
		
		heapq.heappush(priority_q,combined)
	
	root = priority_q[0]
	code_dict = build_code(root)
	return code_dict
	
def build_code(node,code="",code_dict=None):
	if code_dict is None:
		code_dict={}
	if node is not None:
		if node.char is not None:
			code_dict[node.char]= code or 0
		build_code(node.left,code+"0",code_dict)		
		build_code(node.right,code+"1",code_dict)
	return code_dict
	
if __name__ == "__main__":
    
    char_frequencies = {
        "h": 2,
        "u": 1,
        "f": 2,
        "m": 1,
        "a": 1,
        "n": 2,
        " ": 2,
        "c": 1,
        "o": 1,
        "d": 1,
        "i": 2,
        "s": 1,
        "!": 1,
    }
    code_dict = huffman_tree(char_frequencies)
    print("Huffman Codes:", code_dict)