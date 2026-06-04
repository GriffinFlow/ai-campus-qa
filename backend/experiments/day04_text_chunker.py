chunk_size = 200
overlap = 50
with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\cleaned_sample.txt", 'r', encoding='utf-8') as reader:
    raw_text = reader.read()
    text_length = len(raw_text)

chunks_repository = []
chunks_counter = 1
start = 0

while start < text_length:
    ideal_end = start + chunk_size
    end = min(ideal_end, text_length)
    chunk_text = raw_text[start:end]
    current_chunk = {'chunk_id': chunks_counter,
                     'start': start,
                     'end': end,
                     'text': chunk_text
                     }
    chunks_repository.append(current_chunk)#append方法不知道
    print("当前块编号：", chunks_counter)
    print("当前文本的长度：", len(chunk_text))
    print("前十五个字预览：", chunk_text[:15])#这个要咋打印出来啊，不明白。。。
    print()

    if end == text_length:
        break
    else:
        start = end - overlap
        chunks_counter += 1

with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\chunks_preview.txt", 'w', encoding='utf-8') as writer:
    #对于 chunks_repository 中的 每一个小小块 (假设变量名叫 chunk):
        #把 chunk 里的 id、start、end 和 text 提取出来
        #格式化成一行优美的文字（例如：[块1] 位置(0-200) 内容: ...）
        #将这行文字 + "\n" 写入到文件中

        for chunk in chunks_repository:
            line = (
            f"[块{chunk['chunk_id']}] "
            f"位置({chunk['start']}-{chunk['end']}) "
            f"内容: {chunk['text']}\n"
        )
            writer.write(line)   

    #这个逻辑我写不出来

