from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import pyPdf, re

k_word=[]
index= {}
# fi= open('not.txt','w')
class FrequencySummarizer:
	def __init__(self, min_cut=0.1, max_cut=0.9):
		"""
		Initilize the text summarizer.
		Words that have a frequency term lower than min_cut 
		or higer than max_cut will be ignored.
		"""
		self._min_cut = min_cut
		self._max_cut = max_cut 
		self._stopwords = set(stopwords.words('english') + list(punctuation))
		
	def fnPDF_FindText(self, xFile, xString):
		# xfile : the PDF file in which to look
		# xString : the string to look for
		
		PageFound = 0
		Pages= []
		pdfDoc = pyPdf.PdfFileReader(file(xFile, "rb"))
		for i in range(0, pdfDoc.getNumPages()):
			content = ""
			content += pdfDoc.getPage(i).extractText() + "\n"
			content1 = content.encode('ascii', 'ignore').lower()
			ResSearch = re.search(xString, content1)
			if ResSearch is not None:
				PageFound = i
				Pages.append(PageFound)
		return Pages
		 

	def _compute_frequencies(self, word_sent):
		""" 
		Compute the frequency of each of word.
		Input: 
		word_sent, a list of sentences already tokenized.
		Output: 
		freq, a dictionary where freq[w] is the frequency of w.
		"""
		freq = defaultdict(int)
		for s in word_sent:
			for word in s:
				if word not in self._stopwords:
					freq[word] += 1
				# frequencies normalization and fitering
		m = float(max(freq.values()))
		for w in freq.keys():
			freq[w] = freq[w]/m
			if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
				del freq[w]
			else:
				arr=self.fnPDF_FindText('shruti.pdf',w)
				'''
				if len(w)==1 :
					if ord(w)>=0 and ord(w)<128 :
						fi.write(w)
						fi.write("  ")
					
						# print w
						# print ": "
						for i in arr:
						
							fi.write(str(i))
							fi.write(",")
						
						fi.write("\n")
										
						index.update({w:arr})
		fi.close()
		'''
		return freq

	def summarize(self, text, n,ext):
		"""
		  Return a list of n sentences 
		  which represent the summary of text.
		"""
		
		sents = sent_tokenize(text.decode('utf-8'))
		assert n <= len(sents)
		word_sent = [word_tokenize(s.lower()) for s in sents]
		self._freq = self._compute_frequencies(word_sent)
		for key in self._freq:
			k_word.append(key)
		print k_word
		ranking = defaultdict(int)
		for i,sent in enumerate(word_sent):
			
			for w in sent:
				if w in self._freq:
					ranking[i] += self._freq[w]
		sents_idx = self._rank(ranking, n)    
		return [sents[j] for j in sents_idx]

	def _rank(self, ranking, n):
		""" return the first n sentences with highest ranking """
		return nlargest(n, ranking, key=ranking.get)