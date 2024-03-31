# class TrieNode():
#     def __int__(self):
#         self.children = {} #a : TrieNode
#         self.word = False 

# class WordDictionary:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         cur = self.root

#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.word = True 
        
#     def search(self, word: str) -> bool:
#         def dfs(j, root):
#             cur = self.root
#             for i in range(len(word)):
#                 # then we will get the character at position i 
#                 c = word[i]

#                 if c == ".":
#                     # bcz cur.children is a hashmap and we want values 
#                     for child in cur.children.values():
#                         # j is the starting index 
#                         # child -> whichever the node we will be iterating 
#                         # we are skipping the dot so it will be i+1 
#                         if dfs(i+1, child):
#                             # ".ab"
#                             return True 
#                     return False 
#                 else:
#                     if c not in cur.children:
#                         return False 
#                     # if it does exists
#                     cur = cur.children[c]
#         return dfs(0, self.root)



# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)

class TrieNode:
    def __init__(self):
        self.children = {} #a: TrieNode 
        self.word = False 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root 

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True 
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root 

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True 
                    return False
                else:
                    if c not in cur.children:
                        return False 
                    cur = cur.children[c]
            return cur.word 
            
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)