class TreeNode:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.children = []
        self.lis_length = 1

def build_lis_tree(current_node, sequence):
    start_index = current_node.index + 1
    
    for i in range(start_index, len(sequence)):
        if sequence[i] > current_node.value:
            child = TreeNode(sequence[i], i)
            current_node.children.append(child)
            
            build_lis_tree(child, sequence)

def find_longest_path(node):
    if not node.children:
        return 1, [node.value]
    
    max_len = 0
    longest_subsequence = []
    
    for child in node.children:
        child_len, child_seq = find_longest_path(child)
        if child_len > max_len:
            max_len = child_len
            longest_subsequence = child_seq
            
    return max_len + 1, [node.value] + longest_subsequence

def solve_lis_with_tree(sequence):
    
    root = TreeNode(float('-inf'), -1) #root dummy
    build_lis_tree(root, sequence)
    
    max_len, subsequence = find_longest_path(root)
    
    return max_len - 1, subsequence[1:]

#eksekusi
input_sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

print("--- HASIL PROGRAM LIS (METODE TREE) ---")
print(f"Urutan Angka Input: {input_sequence}")
length, subseq = solve_lis_with_tree(input_sequence)

print("-" * 40)
print(f"Panjang LIS         : {length}")
print(f"Salah Satu LIS      : {subseq}")
print("-" * 40)
print("Penjelasan: Program ini membangun struktur Tree dimana setiap node")
print("bercabang ke angka-angka selanjutnya yang lebih besar, lalu")
print("mencari kedalaman maksimum dari tree tersebut.")