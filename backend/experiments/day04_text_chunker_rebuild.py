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
        end = min(text_length, ideal_end)
        chunk_text = raw_text[start:end]
        current_chunk = {'chunk_id': chunks_counter,
                         'start': start,
                         'end': end,
                         'text': chunk_text}
        #append表示将新元素追加到列表末尾
        chunks_repository.append(current_chunk)

        print("当前块的编号：", chunks_counter)
        print("当前文本长度", len(chunk_text))
        print("前十五个字的预览：", chunk_text[:15])
        print()

        if end == text_length:
            break
        else:
            start = end - overlap
            chunks_counter += 1

with open(r"E:\GitProjects\ai-campus-qa\backend\experiments\chunks_preview.txt", 'w', encoding='utf-8') as writer:
     for chunk in chunks_repository:
          line = (
               f"[块{chunk['chunk_id']}]"
               f"位置({chunk['start'] - chunk['end']})"
               f"内容:{chunk['text']}\n"
          )
          writer.write(line)

