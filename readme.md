# 使用streamlit搭建博客

原博客使用jekyll构建，为保持md文件不变动写了这部分内容。

## 展示静态文件
markdown里有展示图片的需求，不想使用images挨个写文件。所以使用streamlit的静态文件服务处理这个需求。

- streamlit 读取的静态文件目录地址是固定的：./static/
- 引用文件引用文件有固定的引用前缀：app/static/
- 启用功能启用的方式有三种(任选其一)：
```angular2html
- 在 $CWD/.streamlit/config.toml 的每个项目配置文件中（参考《配置》）在 .streamlit/config.toml 配置文件中的[server]下设置 enableStaticServing=true
- 设置环境变量 STREAMLIT_server_enable_STATIC_SERVING=true
- 命令行 streamlit run your_script.py --server.enableStaticServing true
```

## 未完成
- [ ] 根据categories或者tags进行目录的区分
- [ ] 增加文章查询