import re
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Komoran
from wordcloud import ImageColorGenerator
from PIL import Image # pillow 설치 요망
import nltk
import numpy as np
from bs4 import BeautifulSoup
from gensim.models import word2vec

plt.rc('font', family='Malgun Gothic')

class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.okt = Okt()
        self.stopwords = []
        self.freqtxt = []
###########################################################################################
    def extract_token(self, payload):
        print('>>> text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'{self.texts[:300]}')

    def extract_hanguel(self):
        print('>>> 한글만 추출')
        texts = self.texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]')
        self.texts = tokenizer.sub('', texts)
        print(f'{self.texts[:300]}')

    def conversion_token(self):
        print('>>> 토큰으로 변환')
        self.tokens = word_tokenize(self.texts)
        print(f'{self.tokens[:300]}')

    def compound_noun(self):
        print('>>> 복합명사는 묶어서 fitering 으로 출력')
        print('>>> ex) 삼성전자의 스마트폰은 --> 삼성전자 스마트폰')
        noun_token = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_token.append("".join(temp))
        self.texts = " ".join(noun_token)
        print(f'{self.texts[:300]}')

    def extract_stopword(self, payload):
        print('>>> text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopwords = f.read()
        self.stopwords = self.stopwords.split(' ')
        print(f'{self.stopwords[:10]}')

    def filtering_text_with_stopword(self):
        print('>>> stopword 로 필터링 ')
        self.texts = word_tokenize(self.texts)
        self.texts = [text for text in self.texts
                      if text not in self.stopwords]
    def frequent_text(self):
        print('>>> 빈도수로 정렬 ')
        self.freqtxt = pd.Series(dict(FreqDist(self.texts)))\
            .sort_values(ascending=False)
        print(f'{self.freqtxt[:10]}')

    def draw_wordcloud(self, payload):
        print('>>> 워드크라우드 작성 ')
        filename = payload.context + payload.fname
        wcloud = WordCloud(filename,
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(self.texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
###########################################################################################
    # 문장을 넣어서 단어와 품사를 튜플로 만들어 리스트 형태로 반환
    @staticmethod
    def sentence_pos(sentence):
        print('# before user dic')
        komo = Komoran()
        result = komo.pos(sentence)
        print('전체 확인하기')
        for myitem in result:
            somedata = '단어 : %s, 품사 : %s' % (myitem[0], myitem[1])
            print(somedata)
        print('-' * 30)
        return result

    '''
    리턴값 # before user dic
    [('국정', 'NNG'), ('농', 'NNG'), 
    ('단', 'NNG'), ('태블릿 PC', 'NNP'), (',', 'SP'), 
    ('설', 'NNB'), ('진', 'NNP'), 
    ('욱', 'NA'), (',', 'SP'), ('가나', 'NNP'), ('다라', 'NNP')]
    '''

    @staticmethod
    def pos_to_noun(sentence):
        komo = Komoran()
        print('명사만 추출해보기')
        nouns = komo.nouns(sentence)
        print(nouns)
        return nouns
###########################################################################################
    # word cloud를 생성한다.
    @staticmethod
    def makeWordCloud(context,wordDict,imageFile,fontpath,filename):  # 워드 클라우드
        # 이미지를 넘파이 배열로 바꿉니다.
        
        imageFile=context+imageFile
        fontpath =context+fontpath
        filename =context+filename
        alice_coloring = np.array(Image.open(imageFile))

        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring,
                              relative_scaling=0.2, background_color='lightyellow')
        wordcloud = wordcloud.generate_from_frequencies(wordDict)
        image_colors = ImageColorGenerator(alice_coloring)
        # random_state : 랜덤 상수 지정
        newwc = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(newwc)
        plt.axis('off')
        plt.savefig(filename)
        plt.figure(figsize=(16, 8))

    @staticmethod
    def makeBarChart(context,wordlist,filename):  # 막대 그래프
        filename = context+filename
        # result를 이용하여 막대 그래프를 그려 보세요.
        result = wordlist[0:10]  # 10개 데이터

        barcount = 10  # 막대 갯수 : 10개만 그리겠다.
        xlow, xhigh = - 0.5, barcount - 0.5

        result = wordlist[:barcount]
        chartdata = []  # 차트 수치
        xdata = []  # 글씨
        mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chartdata[idx]) + '건'  # 예시 : 60건
            # 그래프의 위에 "건수" 표시
            plt.text(x=idx, y=chartdata[idx] - 20, s=value, fontsize=8, horizontalalignment='center')

        plt.xticks(range(barcount), xdata, rotation=45)
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)

        plt.title('상위 ' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일이 저장되었습니다.')

    @staticmethod
    def make_wordlist(context,txt,stopwordTxt):

        filename = context +txt
        ko_con_text = open(filename, 'rt', encoding='utf-8').read()

        okt = Okt()
        token_ko = okt.nouns(ko_con_text)

        # 불용어(stopword) : 빈도 수에 상관없이 분석에서 배제할 단어들
        stop_word_file = context +stopwordTxt
        stop_file = open(stop_word_file, 'rt', encoding='utf-8')
        stop_words = [word.strip() for word in stop_file.readlines()]
        # print(stop_words)

        token_ko = [each_word for each_word in token_ko if each_word not in stop_words]

        # nltk : national language toolkit
        # token : 작은 절편
        ko = nltk.Text(tokens=token_ko)

        wordlist = list()  # 튜플(단어, 빈도수)를 저장할 리스트
        # 가장 빈도수가 많은 500개만 추출
        data = ko.vocab().most_common(500)
        # print(data)
        for word, count in data:
            if (count >= 50 and len(word) >= 2):
                wordlist.append((word, count))
        return wordlist

    @staticmethod
    def create_word2vec(context,filename,prepro_file,model_filename):
        myencoding = 'utf-8'
        filename = context +filename
        myfile = open(filename, 'rt', encoding=myencoding)
        soup = BeautifulSoup(myfile, 'html.parser')
        mydata = soup.text
        # print(mydata)

        results = []  # 결과 저장소
        okt = Okt()

        datalines = mydata.split('\n')
        print(len(datalines))

        for oneline in datalines:
            mypos = okt.pos(oneline, norm=True, stem=True)
            # print(mypos)

            imsi = []  # 임시 리스트
            for word in mypos:
                if not word[1] in ['Josa', 'Eomi', 'Punctuation', 'Verb']:
                    if len(word[0]) >= 2:
                        imsi.append(word[0])

            temp = (' '.join(imsi)).strip()
            results.append(temp)
            # break # 차후 삭제 예정

        # print(results)

        # 정제된 파일로 저장하기
        with open(prepro_file, 'wt', encoding=myencoding) as myfile:
            myfile.write('\n'.join(results))

        print(prepro_file + ' 파일 생성됨')

        # word2vec : word(단어)들을 벡터로 만드는 알고리즘
        # vector(벡터) : 크기와 방향을 가지고 있는 단위
        # 스칼라 : only 값
        # 단어들의 유사도 : 코싸인 유사도, 유클리디언 유사도, 맨하탄 유사도

        # LineSentence : 분석을 하기 위한 sentence를 만들어 주는 함수
        data = word2vec.LineSentence(prepro_file)
        print(type(data))

        # Word2Vec : 해당 sentence를 사용하여 word2vec에 대한 모델을 생성해줍니다.
        # size : 벡터의 차원수, window : 윈도우 사이즈, min_count : 버리고자 하는 최소 빈도수
        # sg : 1(skipgram), 0(cbow)
        model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
        print(type(model))

        # 모델을 저장할 때는 save 함수를 사용합니다.
        # 모델 파일은 바이트 형식의 파일입니다.
        model.save(model_filename)
        print(model_filename + ' 파일 생성됨')

        print('finished')
        
    @staticmethod
    def showGraph(bargraph):
        length = len(bargraph)  # 요소 갯수
        # x축에 보이는 글자
        myticks = list(mydata[0] for mydata in bargraph)
        # 그려질 수치 데이터
        chartdata = list(mydata[1] for mydata in bargraph)
        mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#56FFCC', '#00CCFF', '#CCDDEE']

        plt.figure()
        plt.barh(myticks, chartdata, color=mycolor, align='center')
        plt.yticks(range(length), myticks, rotation='10')
        plt.xlim(min(chartdata) - 0.02, max(chartdata) + 0.02)
        filename = 'word2vec_model_01.png'
        plt.savefig(filename)
        print(filename + ' 파일 저장됨')

    @staticmethod
    def makePie(piegraph):
        myticks = list(mydata[0] for mydata in piegraph)
        chartdata = list(mydata[1] for mydata in piegraph)
        mycolor = ['b', 'g', 'r', 'c', 'm']

        plt.figure()
        plt.pie(chartdata, colors=mycolor, labels=myticks, startangle=90, shadow=False,
                explode=(0, 0.05, 0, 0, 0), autopct='%1.2f%%', normalize=True)
        filename = 'word2vec_model_02.png'
        plt.savefig(filename)
        print(filename + ' 파일 저장됨')

        print('finished')
