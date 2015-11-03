

from xml.parsers.expat import ParserCreate

class SaxHandler(object):
	def start_element(self, name, attrs):
		print ('sax: start_element: %s, attrs: %s' % (name, str(attrs)))

	def end_element(self, name):
		print ('sax: end_element: %s' % name)

	def char_data(self, text):
		print ('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/java">Java</a></li>
</ol>
'''

def char_data2(text):
	print ('sax: char_data--2: %s' % text)

handler = SaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
parser.CharacterDataHandler = char_data2

parser.Parse(xml)