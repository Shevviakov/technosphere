mport math
import pandas as pd

def tf_idf (iterable, stop_words=()):
    raw = {}
    num_docs = len(iterable)
    i = 0
    #TF
    for string in iterable:
        words = {}
        for word in string.split():
            if word not in stop_words:
                try:
                    words[word] += 1
                except:
                    words[word] = 1
        max_count = max(words.values())
        for word in words.keys():
            try:
                raw[word][i] = 0.5 + 0.5*words[word]/float(max_count)
            except:
                raw[word] = [0]*num_docs
                raw[word][i] = 0.5 + 0.5*words[word]/float(max_count)
        i += 1
    
    #IDF
    for word in raw:
        idf = math.log(float(num_docs)/(1+len([1 for x in raw[word] if x>0])))
        for i in xrange(len(raw[word])):
            raw[word][i] *= idf
    
    df = pd.DataFrame(raw)
    return df
