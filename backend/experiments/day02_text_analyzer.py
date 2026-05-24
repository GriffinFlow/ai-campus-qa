###开始pytho项目之路###
def count_words_in_file(file_path):
    #建立一个空空但神圣的字典账本准备计数
    word_dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as my_file:
        full_text = my_file.read()

        #加入统计总行数：
        line_count = len(full_text.splitlines())
       
        #加入统计总字符个数：
        char_count = len(full_text)
        
        clean_text = full_text.strip()
        all_words = clean_text.split()

        #加入统计总单词个数：
        word_count = len(all_words)
       
    for word in all_words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    top5 = sorted(word_dictionary.items(), key=lambda item: item[1], reverse=True)[:5]
    return line_count, char_count, word_count, word_dictionary, top5

target_file = r"e:\GitProjects\ai-campus-qa\backend\experiments\sample.txt"
#r表示原始字符串，避免转义字符的干扰
#为了正确运行：方法一：终端的路径得精确到experiments文件夹下才能正确运行！
#方法二：代码里使用绝对路径！注意前面加r的操作！

line_count, char_count, word_count, report, top5 = count_words_in_file(target_file)
print("文本统计结果如下：")
print(f"总行数：{line_count}")
print(f"总字符数：{char_count}")
print(f"总词数：{word_count}")

print("Top5 高频词：")
for word, count in top5:
    print(word, count)
print("文本词频统计结果如下：")
print(report)
