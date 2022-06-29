# 基于知识图谱的影视智能问答系统
  可用于咨询影视领域知识的问答系统，知识库采取neo4j的图数据库存储实体与其关系，系统主体采用规则式模板匹配，提供模板以内的各种单轮次对话。
  
  关于主体部分的讲解：（原作者）  
  https://www.bilibili.com/video/BV1ca4y1H7Ja?p=2&spm_id_from=333.880.my_history.page.click  
  
  本demo个人在学习过程中进行了一定的魔改，包括但不限于主体部分，添加前端UI界面以及前后端对接使之成为一个完整的QA系统。  
  
  这里附上前端```vue-bot-ui```的原仓库：  
  https://github.com/juzser/vue-bot-ui  
  
  后端采用flask
  
## 效果演示
  <div align=center>
    <src="https://github.com/Pineapple274/-/blob/main/KBQA.gif"/>
  </div>
## 整体架构
```
KBQA_backend
  ├── 建立词表.py     // 建立词表的程序文件
  ├── 建立图谱.py     // 建立知识图谱的程序文件
  ├── FLASK.py       //后端文件用于与
  ├── chatbot_graph.py     // 聊天系统主函数文件/运行文件
  ├── question_classifier.py        // 聊天系统问题分类函数 
  ├── question_parser.py        // 聊天系统问题转换函数 
  ├── answer_search.py        // 聊天系统问题回复函数
  ├── genre.txt        // 建立的词表 
  ├── movie.txt        // 建立的词表  
  ├── person.txt        // 建立的词表  
  └── data   //数据文件
      └── genre.csv               // 图谱数据集之一
      └── movie_to_genre.csv               // 图谱数据集之一
      └── movie.csv               // 图谱数据集之一
      └── person_to_movie.csv               // 图谱数据集之一
      └── person.csv               // 图谱数据集之一
      └── userdict3.txt               // 图谱数据集之一
      └── vocabulary.txt              // 图谱数据集之一
      └── question              // 问题模版（项目中未用，但参考了）
          └── ...              // 16个问题模版
KBQA_vue-bot-ui
  ├── ...            //其他项目文件
  ├── package.json   //依赖与脚本描述文件
  ├── dist           //构建文件夹
  └── src            //项目文件夹
      └── App.vue              //核心前端文件
      └── ...                  //其他
```

## 构建策略
  此处环境需要：
  ```
  node.js vue neo4j python ( py2neo flask flask_cors pyahocorasick )
  ```
  
### 前端部分
  在KBQA_vue-bot-ui目录下  
  安装依赖：```npm install```
  前端发布：```npm run serve```（此处也可构建项目后发布，相关请自行调整）
  
### 后端部分
  在KBQA_backend目录下    
  后端部署：```python FLASK.py```
  
### 数据库部分
  在neo4j文件中的bin目录下  
  ```neo4j.bat console```(windows10环境下）  
  ```./neo4j console```（unix环境下）  
  
### 基础构建❤️
  向neo4j数据库中写入实体与实体关系    
  （这里需要注意的是，首次运行neo4j需要通过浏览器访问所发布的地址进行密码重置，并将重置密码与项目路径更新至构建图谱.py文件中）  
  
  ```python 构建图谱.py```
  
  之后便可通过前端页面（具体地址参考前端部分所发布的地址与端口）访问系统  
  
  
  
