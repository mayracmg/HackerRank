import re

def detect_html_attributes(html):
    all_tags = {}
    
    tags = re.findall(r'<[\w].*?>', html)
    
    for tag in tags:
        tag_name = (str(re.findall(r'<[\w]+', tag)[0])).replace('<', '')
         
        attributes = re.findall(r'\s+[\w]+=', tag)
        attributes = [str(a).strip().replace('=', '') for a in attributes]
        
        try:
            all_tags[tag_name] = all_tags[tag_name] + attributes
        except:
            all_tags[tag_name] = attributes
    
    for tag, attrs in sorted(all_tags.items()):   
        attributes = ','.join(sorted(set(attrs))) if attrs != None else ''
        print(tag + ":" + attributes)

if __name__ == '__main__':
    n = int(input())
    html = ''
    for _ in range(n):
        html += input()
    detect_html_attributes(html)
