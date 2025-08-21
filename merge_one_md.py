from pathlib import Path

all_str = ''
for file_name in ['c1.md','c2.md','c3.md','c4.md','c5.md','c6.md','c7.md','c8.md','c9.md','c10.md',]:
    str1 = Path(r'D:\codes\nb_log_readdocs\source\articles').joinpath(file_name).open('r',encoding='utf-8').read()
    all_str += str1

if __name__ == '__main__':
    print(len(all_str))
    Path(__file__).parent.joinpath('nb_log_merge_docs.md').write_text(all_str,encoding='utf-8')