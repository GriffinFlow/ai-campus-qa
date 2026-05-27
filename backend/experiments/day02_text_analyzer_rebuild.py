def count_words_in_file(file_path):
    word_dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as my_file:
        full_text = my_file.read()
        #统计总行数
        line_count = len(full_text.splitlines())
        #统计总字符数
        char_count = len(full_text)

        #开始对它洗澡更衣
        clean_text = full_text.strip()
        all_words = clean_text.split()

        #统计总单词数
        word_count = len(all_words)

    for word in all_words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
            #python对对齐格式的要求很严格，如果没对好就会报错显示红色或黄色，so语句要写在哪里和哪里对齐要理解。

    top5 = sorted(word_dictionary.items(), key=lambda item : item[1], reverse=True)[:5]
    #word_dictionary.items()意思是把字典变成一堆(单词,次数)的配对
    #sorted指排序, key指定按谁排, reverse=True指倒序
    #lambda item: item[1]是一个临时小函数，意为取配对里的第2个元素作为排序依据
    #[:5]指切片，取前5个
    #小口诀：配对排，按次数，倒着来，切五个。
    
    return line_count, word_count, char_count, word_dictionary, top5

#绝对路径
file_path = r"e:\GitProjects\ai-campus-qa\backend\experiments\sample.txt"
#r表示原始字符串，避免转义字符的干扰
line_count, word_count, char_count, word_dictionary, top5 = count_words_in_file(file_path)
print("文本统计结果如下：")
print(f"总行数：{line_count}")
print(f"总字符数：{char_count}")
print(f"总单词数：{word_count}")

print("top5高频词数：")
for word, count in top5:
    print(word, count)
print("文本词频统计结果如下：")
print(word_dictionary)