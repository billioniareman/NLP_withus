from nltk.tokenize import sent_tokenize, word_tokenize
text="I am a random TEXT generated for TEXT summerization. Consider me a medical demo TEXT. let abbriviation be NLP at first"
abb=["NLP"]
output=[]
tokens=text.split(" ")
class LowerCase:
    def lower_case(text):
        for token in tokens:
            if token in abb:
                output.append(token)
            else:
                output.append(token.lower())
        return " ".join(output)
    
class tokenization:
    def tokenizer(text):
        sentences=sent_tokenize(text)
        print(sentences)
        for sentence in sentences:
            words=word_tokenize(sentence)
            print(words)
        return sentences,words