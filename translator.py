from googletrans import Translator

translator = Translator()

sentence = input("번역을 원하는 문장을 입력해주세요 : ")

result = translator.translate(sentence,'en') # 국가마다 코드가 다름
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=================================")