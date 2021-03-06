# - 文本文件input.txt由若干英文单词和分隔符（空格、回车、换行）组成，根据如下说明编写程序统计不同单词出现的次数（频度）。将统计结果按出现频度从高到低排序，并将出现频度大于5的单词及其频度输出到文件output.txt中。
# - 文件格式单词,次数，每个单词占一行
# - 多个连续分隔符被视为一个分隔符
# - 大小写敏感，即大小写不同的为两个单词
# - 每个单词长度不超过20个字符
# - 单词的数量未知，使用静态大数组将扣5分

class Solution(object):
    def __init__(self):
        self.words = []
        self.word_dict = dict()
        self.read_file_construct_dict()
        self.construct_dict()
        self.sort_dict()
        self.write_file()

    def read_file_construct_dict(self):
        with open('../../Data/input.txt') as fb:
            for line in fb:
                wordList = line.split()
                self.words.extend(wordList)

    def construct_dict(self):
        for word in self.words:
            if word not in self.word_dict:
                self.word_dict.setdefault(word, 0)
            self.word_dict[word] += 1

    def sort_dict(self):
        self.word_dict = sorted(self.word_dict.items(), key=lambda item: -item[1])

    def write_file(self):
        with open('./output.txt', 'w') as fb:
            for item in self.word_dict:
                if item[1] > 5:
                    fb.write("{:} {:}\n".format(item[0], item[1]))


if __name__ == '__main__':
    solution = Solution()
