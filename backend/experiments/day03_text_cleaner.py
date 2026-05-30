
with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\dirty_sample.txt", 'r', encoding='utf-8') as reader:
        with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\cleaned_sample.txt", 'w', encoding='utf-8') as writer:
            for line in reader:
                clean_line = ' '.join(line.split())
                if clean_line == "":
                    continue
                else:
                    writer.write(clean_line + "\n")
