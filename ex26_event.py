

from html.parser import HTMLParser
from html.entities import name2codepoint

class EventHtmlParser(HTMLParser):

	def __init__(self):
		super(EventHtmlParser, self).__init__()

		self.event_list = []
		self.event_location = []
		self.event_time = []
		self.target = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'h3' and ('class', 'event-title') in attrs:
			self.target = 'event_list'
		if self.target == 'event_list' and tag == 'a':
			self.target = 'event_list_a'
		
		if tag == 'span' and ('class', "event-location") in attrs:
			self.target = 'event-location'

		if tag == 'time':
			self.target = 0
			if tag == 'span':
				pass




	def handle_data(self, data):
		if self.target == 'event_list_a':
			self.event_list.append(data)
			# print (self.event_list)
			self.target = ''
		elif self.target == 'event-location':
			self.event_location.append(data)
			# print (self.event_location)
			self.target = ''
		elif isinstance(self.target, int) and self.target < 3:
			self.event_time.append(data.strip())
			# print (self.event_time)
			self.target += 1
		elif self.target == 3:
			self.target = ''
			# print (self.event_time)




parser = EventHtmlParser()
with open('index.html') as html_Text:
	parser.feed(html_Text.read())

# llen = len(parser.event_time)
# event_time = []

# for i in range(int(llen/3)):
# 	event_time.append(parser.event_time[3*i+0] + '-' + parser.event_time[i*3 + 1] + ' ' + parser.event_time[3*i + 2])

# print (event_time)

# class EventIterm(object):

# 	def __init__(self):
# 		self.event_title = None
# 		self.event_location = None
# 		self.event_time = None

event_list = []

for i in range(len(parser.event_list)):
	# iterm = EventIterm()
	# iterm.event_title = parser.event_list[i]
	# iterm.event_time = parser.event_time[i]
	# iterm.event_location = parser.event_location[i]
	# event_list.append(
	# {
	# 	'event_title': iterm.event_title,
	# 	'event_time': iterm.event_time,
	# 	'event_location': iterm.event_location
	# })
	event_list.append(
	{
		'event_title': parser.event_list[i],
		'event_time': parser.event_time[3*i+0] + '-' + parser.event_time[i*3 + 1] + ' ' + parser.event_time[3*i + 2],
		# 'event_time': parser.event_time[i],
		'event_location': parser.event_location[i]
	})

print (event_list)
