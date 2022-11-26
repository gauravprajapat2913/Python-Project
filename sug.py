from nltk.collocations import TrigramCollocationFinder # Word Prediction Module
from nltk.tokenize import word_tokenize  # Word Tokenize Module
import pandas as pd 

def file_write(a): # File to Store Data
    p = open("all_data.txt","a")
    p.write(text)
    p.close()

def file_read():  # File Read and Store in Variable
    q = open("all_data.txt","r")
    data = q.read()
    q.close()
    return data
    
    
text = ""
for i in range(1,5):  # Enter Text 
    var = input("Enter your Text : ")
    text = text +" "+var

file_write(text)
data_txt = file_read()

# Word Prediction
first,second,third,count = [],[],[],[]
f = TrigramCollocationFinder.from_words(word_tokenize(data_txt))
for i in f.ngram_fd.items():
    try :
        first.append(i[0][0])
        second.append(i[0][1])
        third.append(i[0][2])
        count.append(i[1])
    except :
        pass

# Make dataset 
dataset = pd.DataFrame({"First":first,"Second":second,"Third":third,"Count":count})
dataset = dataset.sort_values(by="Count",ascending=False)

print()
print()

# New text Insert
new_text = input("enter new text : ")
index_no = dataset[dataset['First'] == new_text].index[0]

# Word Prediction Output
print(dataset["Second"][index_no],dataset["Third"][index_no])