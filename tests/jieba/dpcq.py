
import jieba

fo = open('doupocq.txt', 'r+')

txt = fo.read()

seg_list = jieba.cut_for_search(txt)  # 搜索引擎模式
print(", ".join(seg_list))

