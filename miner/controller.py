import nltk
from miner.entity import Entity
from miner.service import Service
from gensim.models import word2vec

class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        entity.fname = 'kr-Report_2018.txt'
        entity.context = './data/'
        service.extract_token(entity)
        service.extract_hanguel()
        service.conversion_token()
        service.compound_noun()
        entity.fname = 'stopwords.txt'
        service.extract_stopword(entity)
        service.filtering_text_with_stopword()
        service.frequent_text()
        entity.fname = 'D2Coding.ttf'
        service.draw_wordcloud(entity)

    @staticmethod
    def loop1():
        sentence = '세일즈 우먼인 아름다운 그녀가 아버지 가방에 들어 가시나 ㅎㅎ'
        Service.sentence_pos(sentence)
        Service.pos_to_noun(sentence)

    @staticmethod
    def loop2():
        txt='tojiText.txt'
        context = './data/'
        stopwordTxt= 'stopword.txt'
        wordlist=Service.make_wordlist(context,txt,stopwordTxt)
        fontpath = 'malgun.ttf'
        filename = 'tojiWordCloud.png'
        imageFile ='alice_color.png'
        wordDict = dict(wordlist)
        Service.makeWordCloud(context,wordDict,imageFile,fontpath,filename)
        filename = 'tojiBarChart.png'
        Service.makeBarChart(context,wordlist,filename)

    @staticmethod
    def loop3():
        context = './data/'
        prepro_file = 'word2vec.prepro'
        filename = '문재인대통령신년사.txt'
        model_filename = 'word2vec.model'
        Service.create_word2vec(context,filename,prepro_file,model_filename)
        model = word2vec.Word2Vec.load(model_filename)
        print(type(model))

        # most_similar : positive에 명시된 단어에 대하여 유사도가 높은 항목을
        # topn 개만 보여 주세요.
        bargraph = model.wv.most_similar(positive=['국민'], topn=10)
        print(bargraph)

        piegraph = model.wv.most_similar(positive=['남북'], topn=5)
        print(piegraph)

        Service.showGraph(bargraph)

        Service.makePie(piegraph)

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 사전 다운로드')
        print('2. 보고서 분석')
        print('3. 명사만 보여주기')
        print('4. 텍스트로 워드 클라우드와 막대그래프 만들기 심플버전 ')
        print('5. word2vec을 만들고 저장한다.')
        return input('Select Menu\n')
    app = Controller()

    while 1:
        menu = print_menu()

        if menu == '1':
            app.download_dictionary()

        if menu == '2':
            app.data_analysis()

        if menu =='3':
            app.loop1()

        if menu == '4':
            app.loop2()

        if menu == '5':
            app.loop3()
            
        elif menu == '0':
            break