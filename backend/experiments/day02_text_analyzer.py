###开始pytho项目之路###
def count_words_in_file(file_path):
    #建立一个空空但神圣的字典账本准备计数
    word_dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as my_file:
        full_text = my_file.read()

        #加入统计总行数：
        line_count = full_text.count('\n') + (1 if full_text else 0)#如果文本不为空，则行数为换行符数量加1，否则为0
        print("文本总行数：")
        print(line_count)

        #加入统计总字符个数：
        char_count = len(full_text)
        print("文本总字符个数：")
        print(char_count)

        clean_text = full_text.strip()
        all_words = clean_text.split()

        #加入统计总单词个数：
        word_count = len(all_words)
        print("文本总单词个数：")
        print(word_count)
    for word in all_words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return word_dictionary

target_file = r"e:\GitProjects\ai-campus-qa\backend\experiments\sample.txt"
#r表示原始字符串，避免转义字符的干扰

report = count_words_in_file(target_file)
print("文本词频统计结果如下：")
print(report)
#为了正确运行：方法一：终端的路径得精确到experiments文件夹下才能正确运行！
#方法二：代码里使用绝对路径！注意前面加r的操作！