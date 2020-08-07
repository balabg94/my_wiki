import os

this_folder = os.path.dirname(os.path.abspath(__file__))
pages_path = os.join(this_folder, 'pages')


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
	except FileNotFoundError:		
		content="No information on this topic"
		
	return content

def list_topics():
    pages=os.listdir(pages_path)
    topics = []
    for page in pages:
        topics.append(os.path.splitext(page)[0])
    return topics
