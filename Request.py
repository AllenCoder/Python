from lxml import html
import requests

page = requests.get('http://www.devcoder.cn')
tree = html.fromstring(page.text)

title = tree.xpath('/html/head/title/text()')
print(title)