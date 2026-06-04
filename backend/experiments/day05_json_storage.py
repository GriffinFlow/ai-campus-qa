import json
with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\cleaned_sample.txt", 'r', encoding='utf-8') as reader:
    raw_text = reader.read()
    text_length = len(raw_text)

    chunk_size = 200
    overlap = 50

    all_chunks_list = []
    start = 0
    chunks_counter = 1
while start < text_length:
    ideal_end = start + chunk_size
    end = min(text_length, ideal_end)
    chunk_text = raw_text[start:end]
    current_len = len(chunk_text)
    info = {
        'chunk_id': chunks_counter,
        'start': start,
        'end': end,
        'length': current_len,
        'text': chunk_text
    }
    all_chunks_list.append(info)

    if end == text_length:
        break
    else:
        start = end - overlap
        chunks_counter += 1

print("正在将数据打包成标准集装箱...")

with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\chunks.json", 'w', encoding='utf-8') as json_file:
    json.dump(all_chunks_list, json_file, ensure_ascii=False, indent=2)

print("保存成功！集装箱chunks.json已生成。")

print("正在启动下游验证程序...")

with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\chunks.json", 'r', encoding='utf_8') as read_file:
    loaded_data = json.load(read_file)
    total_chunks = len(loaded_data)

print("---下游系统验证成功---")

print("成功读取到的chunk总数为：", total_chunks)

if total_chunks > 0:
    print("为你展示第1个切块的黄金元数据字典：")
    print(loaded_data[0])

