import os
import csv

# 需要查找的原文
search_texts = [
    "原文"

]

# src目录
src_root = r".\src"

result_files = []

# 递归遍历所有 .cpp / .h
for dirpath, _, filenames in os.walk(src_root):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        if ext not in (".cpp", ".h", ".rc"):
            continue
        fullpath = os.path.join(dirpath, filename)
        try:
            with open(fullpath, "rt", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for s in search_texts:
                    if s in content:
                        result_files.append(fullpath)
                        break
        except:
            continue

# 去重并排序
result_files = sorted(list(set(result_files)))

# 输出 translate_list.csv
csv_name = "translate_list.csv"
with open(csv_name, "w", newline="", encoding="utf-8-sig") as csvf:
    writer = csv.writer(csvf)
    writer.writerow(["file_path"])
    for fp in result_files:
        writer.writerow([fp])

print("✅ 扫描完成，匹配到的文件列表：")
for f in result_files:
    print(f)
print(f"\n📄 文件列表已写入：{csv_name}")
