# "0123456789" \
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
# "abcdefghijklmnopqrstuvwxyz" \
# "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúý" \
# "ĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặ" \
# "ẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợ" \
# "ỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ"

class Node:
    # Contructor
    def __init__(self):
        self.children = [None] * 196
        self.isEnd = False


class PrefixTree:
    dict_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
             'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
             'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36,
             'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45,
             'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54,
             't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61, 'À': 62, 'Á': 63,
             'Â': 64, 'Ã': 65, 'È': 66, 'É': 67, 'Ê': 68, 'Ì': 69, 'Í': 70, 'Ò': 71, 'Ó': 72,
             'Ô': 73, 'Õ': 74, 'Ù': 75, 'Ú': 76, 'Ý': 77, 'à': 78, 'á': 79, 'â': 80, 'ã': 81,
             'è': 82, 'é': 83, 'ê': 84, 'ì': 85, 'í': 86, 'ò': 87, 'ó': 88, 'ô': 89, 'õ': 90,
             'ù': 91, 'ú': 92, 'ý': 93, 'Ă': 94, 'ă': 95, 'Đ': 96, 'đ': 97, 'Ĩ': 98, 'ĩ': 99,
             'Ũ': 100, 'ũ': 101, 'Ơ': 102, 'ơ': 103, 'Ư': 104, 'ư': 105, 'Ạ': 106, 'ạ': 107,
             'Ả': 108, 'ả': 109, 'Ấ': 110, 'ấ': 111, 'Ầ': 112, 'ầ': 113, 'Ẩ': 114, 'ẩ': 115,
             'Ẫ': 116, 'ẫ': 117, 'Ậ': 118, 'ậ': 119, 'Ắ': 120, 'ắ': 121, 'Ằ': 122, 'ằ': 123,
             'Ẳ': 124, 'ẳ': 125, 'Ẵ': 126, 'ẵ': 127, 'Ặ': 128, 'ặ': 129, 'Ẹ': 130, 'ẹ': 131,
             'Ẻ': 132, 'ẻ': 133, 'Ẽ': 134, 'ẽ': 135, 'Ế': 136, 'ế': 137, 'Ề': 138, 'ề': 139,
             'Ể': 140, 'ể': 141, 'Ễ': 142, 'ễ': 143, 'Ệ': 144, 'ệ': 145, 'Ỉ': 146, 'ỉ': 147,
             'Ị': 148, 'ị': 149, 'Ọ': 150, 'ọ': 151, 'Ỏ': 152, 'ỏ': 153, 'Ố': 154, 'ố': 155,
             'Ồ': 156, 'ồ': 157, 'Ổ': 158, 'ổ': 159, 'Ỗ': 160, 'ỗ': 161, 'Ộ': 162, 'ộ': 163,
             'Ớ': 164, 'ớ': 165, 'Ờ': 166, 'ờ': 167, 'Ở': 168, 'ở': 169, 'Ỡ': 170, 'ỡ': 171,
             'Ợ': 172, 'ợ': 173, 'Ụ': 174, 'ụ': 175, 'Ủ': 176, 'ủ': 177, 'Ứ': 178, 'ứ': 179,
             'Ừ': 180, 'ừ': 181, 'Ử': 182, 'ử': 183, 'Ữ': 184, 'ữ': 185, 'Ự': 186, 'ự': 187,
             'Ỳ': 188, 'ỳ': 189, 'Ỵ': 190, 'ỵ': 191, 'Ỷ': 192, 'ỷ': 193, 'Ỹ': 194, 'ỹ': 195}

    # Contructor
    def __init__(self):
        self.root = self.getNode()

    def __str__(self, trie, string, level):
        # If Node is a endWay so print string,
        # else just go and go :D
        if self.isLeafNode(trie):
            string[level] = None
            s = ''.join([str(elem) for elem in string if elem is not None])
            print(s)

        for i in range(196):
            # print(self.get_key(i))
            if trie.children[i]:
                string[level] = self.get_key(i)
                self.__str__(trie.children[i], string, level + 1)
                string[level] = None

    def getNode(self):
        return Node()

    def _charToIndex(self, ch):
        return self.dict_[ch] - self.dict_['0']

    def isLeafNode(self, trie):
        return trie.isEnd is not False

    def get_key(self, val):
        for key, value in self.dict_.items():
            if val == value:
                return key

        return None

    def insert(self, key):
        # If not present in Trie, add key
        # If the key is prefix of trie node,
        # marks leaf node
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])

            # If current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()

            # Go next level
            pCrawl = pCrawl.children[index]

        # Mark last node as leaf
        pCrawl.isEnd = True

    def delete(self, key):
        # Delete key in Trie
        pCrawl = self.root
        length = len(key)
        if self.search(key):
            for i in range(length):
                index = self._charToIndex(key[i])
                pCrawl = pCrawl.children[index]
            pCrawl.isEnd = False

    def search(self, key):
        # Search key in Trie
        # Return True if key is presents in Trie,
        # else False
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl is not None and pCrawl.isEnd

    def isPrefix(self, key):
        # Check if key is Prefix in Trie
        # Return True | False
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])

            # check character
            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]
        return True

def main():

    keys = ["lapin", "laper", "lopin", "louve", "loup", "loupe", "ma"]

    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = PrefixTree()

    # Construct trie
    for key in keys:
        t.insert(key)

    level = 0
    string = [None for i in range(20)]

    # Display trie
    # t.display(t.root, string, level)
    print(t.__str__(t.root, string, level))
    # Search for different keys
    print("{} ---- {}".format("loup", output[t.search("loup")]))
    # Delete some keys and search again
    t.delete("loup")
    print("{} ---- {}".format("loupe", output[t.search("loupe")]))



if __name__ == '__main__':
    main()
