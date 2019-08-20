import re

f = open('dic_noun.txt')
dic_data = f.read().split('\n')
# print(dic_data[3])

# x = areas[2].find('品詞 (')
words = []
#words_ = []
i = 0

for dic in dic_data:
    w = dic.split(',')

    #if -1 != w[0].find('名詞 一般'):
    if re.match(r'名詞 一般', w[0]):
        if not w[1]:
            print("空文字発見")
        else:
            words.append(w[1])
            #words_.append(w[1])
            i += 1

print("input words : " + str(i))
#str_ = '\n'.join(words_)
#with open("code_words.txt", 'wt') as f:
#    f.write(str_)

f.close()