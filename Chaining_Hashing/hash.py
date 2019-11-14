import hashlib
import time
from argparse import ArgumentParser


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def __repr__(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
        return ''

    def search_target(self, target):
        current_node = self.head
        if current_node.data == target:
            return True
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data == target:
                return True
        return False

    def is_empty(self):
        return True if (self.head.next is None and self.head.data is None) else False



class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size
        self.collision_count = 0

    def __repr__(self):
        for i in range(self.size):
            print(self.map[i], end='\n')
        return ''

    def get_hash_md5(self, key):
        words_hash = hashlib.md5(key.encode())
        # Convert to int value from hexadecimal and take mod of table size to hash
        return int(words_hash.hexdigest(), 16) % self.size

    def find_word(self, target):
        word_hash = self.get_hash_md5(target)
        if self.map[word_hash] is None:
            return False
        return self.map[word_hash].search_target(target)

    def add(self, key):
        key_hash = self.get_hash_md5(key)
        key_value = key
        found_flag = False

        if self.map[key_hash] is None:
            self.map[key_hash] = LinkedList()
            self.map[key_hash].append(key_value)
            return True
        else:
            if not self.map[key_hash].search_target(key_value):
                self.collision_count += 1
                self.map[key_hash].append(key_value)
                return True
            else:
                return True


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--size',
        '-s',
        default=1000,
        type=int,
        help='Size of hash map which will be created'
    )
    parser.add_argument(
        '--path',
        '-p',
        type=str,
        default='dict',
        help='Path to file with words for hash map'
    )
    parser.add_argument(
        '--target_word',
        '-w',
        type=str,
        default='woman',
        help='Word that need to be found'
    )

    return parser.parse_args()


def main():
    parser = parse_arguments()
    with open(parser.path, 'r') as file:
        words = file.read().split()
    hash_map_size = parser.size
    h = HashMap(hash_map_size)
    for word in words:
        h.add(word)
    if parser.target_word:
        start_time = time.time()
        if h.find_word(parser.target_word):
            print('The {} is in a hash map, the search time is {}'.format(parser.target_word,
                                                                          "%f ms" % (time.time() - start_time)))
        else:
            print('The {} is not in a hash map, the search time is {}'.format(parser.target_word,
                                                                               "%f ms" % (time.time() - start_time)))
    print("The collision number during adding {} words from the file is: {}".format(parser.size, h.collision_count))


if __name__ == '__main__':
    main()
