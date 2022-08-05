import collections
import math
from typing import List


class TfIdf:
    def __init__(self, Docs: List[List[str]]):
        """Docs - list of documents with tokens. 
        example: [['doc1_word1', 'doc1_word2'], ['doc2_word1', 'doc2_word2']]"""
        self.docs = Docs
        self.n = len(Docs)
        self.predata_docs_dict = self.calc_predata_docs(self.docs)
        self.m = self.calc_m(self.predata_docs_dict)
        
        
    def calc_predata_docs(self, docs):
        """calc meta_data"""
        predata_docs = {}
        for index,v in enumerate(docs):
            for i_ in v:
                if predata_docs.get(i_, False):
                    current_value_count = predata_docs[i_]['count']
                    current_value_docs  = predata_docs[i_]['docs_num']
                    current_value_docs.append(index)
                    predata_docs[i_] = {'count': current_value_count + 1, 'docs_num':  current_value_docs}
                else:
                    current_value_count = 1
                    current_value_docs  = [index]
                    predata_docs[i_] = {'count': current_value_count, 'docs_num':  current_value_docs}
        return predata_docs

    def calc_m(self, predata_docs_dict):
        """Count all words."""
        m_value = sum([i['count'] for i in predata_docs_dict.values()])
        return m_value


    def calc_tf(self, item_docs: List[str]):
        """Calculate term frequency."""
        counter = dict(collections.Counter(item_docs))
        for token, count_value in counter.items():
            # calculation formula ->
            counter[token] = count_value/len(item_docs)
        return counter
    
    def calc_idf(self, token):
        """Calculate inverse document frequency."""
        # calculation formula ->
        idf = math.log10(len(self.docs)/self.predata_docs_dict.get(token)['count'])
        return idf
    
    def calc_tf_idf(self):
        """Finnaly calculation."""
        result = []
        for i in self.docs:
            calc_tf_item = self.calc_tf(i)
            for i_ in calc_tf_item.keys():
                # calculation formula ->
                calc_tf_item[i_] = calc_tf_item[i_] * self.calc_idf(i_)
            result.append(calc_tf_item)
        return result
