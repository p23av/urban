class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        dict_ = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                all_words = file.read().lower()
                for char_ in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    all_words.replace(char_, '')
                all_words = all_words.split()
                dict_[file_name] = all_words
        return dict_

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            idx = words.index(word.lower()) + 1
            dict_[name] = idx
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            count = len(list(filter(lambda w: w == word.lower(), words)))
            dict_[name] = count
        return dict_
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# name = 'sample.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')