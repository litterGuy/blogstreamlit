import os

import streamlit as st
from streamlit_option_menu import option_menu

from md import parse_md_header, get_md_content


def initWebsite(folder_path):
    st.set_page_config("博客", "random", initial_sidebar_state="expanded")

    mds = get_markdown_categories(folder_path)
    options = [t['title'] for t in mds]
    mdsDict = {t['title']: t for t in mds}

    with st.sidebar:
        selected_page = option_menu('文章列表', options=options, default_index=0)

    if selected_page in mdsDict:
        md = mdsDict[selected_page]
        mdpath = md['file_path']
        content = get_md_content(mdpath)
        st.text('分类：'+', '.join(md['categories']))
        st.text('标签：'+', '.join(md['tags']))
        st.text('发布时间：'+md['date'].strftime('%Y-%m-%d %H:%M:%S'))
        st.markdown(content, unsafe_allow_html=True)


# 解析所有markdown信息
@st.cache_data
def get_markdown_categories(folder_path):
    markdown_files = []
    files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    if len(files) == 0:
        return markdown_files
    for file in files:
        mdinfo = parse_md_header(os.path.join(folder_path, file))
        markdown_files.append(mdinfo)
    # 根据时间排序
    sorted_tuples = sorted(markdown_files, key=lambda x: x['date'], reverse=True)
    return sorted_tuples


if __name__ == '__main__':
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "markdown")
    initWebsite(folder_path)
