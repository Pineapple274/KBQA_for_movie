from re import A
from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        no_answer = '没能理解您的问题，请参考可行的问题模板'
        res_classify = self.classifier.classify(sent)

        if not res_classify:
            return no_answer
        #print('类别：',res_classify)
        res_sql = self.parser.parser_main(res_classify)
        
        #print('sql语句',res_sql)
        
        answers = self.searcher.search_main(res_sql)
        
        return answers
     #   if final_answers == '':
     #       print(answer)
      #  else:
       #     print(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    question = input('Hello，欢迎咨询电影话题，请输入您的问题\n')
    print(handler.chat_main(question)[0].strip())
    while 1:
        question = input('您还有什么问题吗？\n')
        print(handler.chat_main(question)[0].strip())



