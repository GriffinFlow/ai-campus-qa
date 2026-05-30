
#记录一共读了多少行
total_lines = 0
#记录一共发现了多少个烂空行
blank_lines = 0
#记录最终成功保留了多少行
valid_lines = 0

with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\dirty_sample.txt", 'r', encoding='utf-8') as reader:
        with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\cleaned_sample.txt", 'w', encoding='utf-8') as writer:
            for line in reader:
                total_lines += 1
                line = line.lower()
                clean_line = ' '.join(line.split())
                if clean_line == "":
                    blank_lines += 1
                    continue
                else:
                    valid_lines += 1
                    writer.write(clean_line + "\n")

print("------ 清洗工作汇报 ------")
print("原始文件总行数:", total_lines)
print("过滤掉的空行数:", blank_lines)
print("最终保留的有效行数:", valid_lines)
