import os

import yaml


# 解析md文件头部
def parse_md_header(file_path):
    yaml_content, _ = get_md(file_path)

    # 把文件路径也放置到结果中
    yaml_content['file_path'] = file_path

    return yaml_content


def get_md_content(file_path):
    _, content = get_md(file_path)
    return content


# 获取md内容
def get_md(file_path):
    # 使用UTF-8-sig打开文件，去除掉\ufeff、\xa0、\u3000等字符
    with open(file_path, 'r', encoding='UTF-8-sig') as file:
        lines = file.readlines()

    yaml_content = []
    in_yaml = False

    for line in lines:
        if line.strip() == '---':
            if not in_yaml:
                in_yaml = True
            else:
                in_yaml = False
                break

        if in_yaml:
            yaml_content.append(line)

    yaml_content = ''.join(yaml_content)
    yaml_data = yaml.safe_load(yaml_content)

    # 提取正文内容
    content = ''.join(lines[lines.index('---\n', 1) + 1:])

    return yaml_data, content


if __name__ == '__main__':
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "markdown")
    yc, ct = get_md(os.path.join(folder_path, "2019-04-17-ConcurrentHashMap.md"))
    print(yc, ct)
