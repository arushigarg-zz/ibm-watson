from sum import FrequencySummarizer
from flask import render_template, request
import doc_text
import convert


# @app.route() mappings start here

# @app.route('/', methods=['GET', 'POST'])
def main_sum(filename,nol):
	# # if request.method == 'GET':
		# # return render_template('home.html')
	# elif request.method== 'POST':
		# filename = request.form.get('file',None)
		# nol =  int(request.form.get('nol',None))
	s=doc_text.document_to_text(filename,'C:\Python27\\atson\uploads\\'+filename)
	# print s
	ext= filename.rsplit('.', 1)[0]
	with open(ext+'.txt', 'r') as f:
		first_line = f.readline()
	f.close()
	#convert
	f= open(ext+'.txt','r')
	text= f.read()	
	fre= FrequencySummarizer()
	# print nol
	arr=fre.summarize(text,nol,ext)
	file= open(ext+'o.txt','w')
	heading='SUMMARY OF '+first_line+'\n'
	file.write(heading)
	for strng in arr:
		if type(strng) is bool:
			file.write(strng)
		else:
			if len(strng)==1 and ord(strng)<128 and ord (strng)>=0:
				file.write("  ")
			else :
				file.write(strng.encode('utf-8'))
				file.write("\n")
		
	pdfclass=convert.pyText2Pdf(ext+'o.txt',ext+'o.pdf')
	pdfclass.parseArgs()
	pdfclass.Convert()
	return render_template('download.html')
	file.close()	
	return ext+"o.pdf"
		#return fre.summarize(text,2)
		#return render_template('form.html', form=form)



if __name__ == "__main__":
	app.run(debug=True)
