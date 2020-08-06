import os

pages_path='pages'

def save_page(title, content):
	file_name=title+'.txt'
	file_path=os.path.join(pages_path, file_name)
	
	f=open(file_path, 'w+')
	f.write(content)
	print("Saved")
	
def load_page(title):
	file_name=title+'.txt'
	file_path=os.path.join(pages_path, file_name)
	try:
		f=open(file_path, 'r')
		content= f.read()
		1+'2'
	except FileNotFoundError:		
		content="No information on this topic"
		
	return content

def list_topics():
	pages=os.listdir('pages')
	out= ','.join(pages)
	return out
