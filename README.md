# efb-keyword_prompt-middleware

关键字提示的插件
直接改keywords的列表内容即可，默认只有红包提示，我只是写来抢红包的~~

使用方法：

1、把__init.py__丢进`models/blueness/`

2、在配置文件`profiles/default/config.yaml`中添加

```
middlewares:
  - blueness.KeywordPromptMiddleware
```

3、修改`__init.py__`中`keywords`的关键字，默认只有红包的提示
