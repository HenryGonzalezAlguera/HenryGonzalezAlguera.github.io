"""Minimal zero-dependency static checks for the personal portfolio."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.local_paths = []
        self.anchors = []
        self.projects = 0
        self.has_main = False
        self.has_h1 = False
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get('id'):
            self.ids.add(attributes['id'])
        if tag == 'main': self.has_main = True
        if tag == 'h1': self.has_h1 = True
        if tag == 'article' and 'project-card' in attributes.get('class','').split():
            self.projects += 1
        if tag == 'a' and attributes.get('href','').startswith('#'):
            self.anchors.append(attributes['href'][1:])
        if tag in ('link','img','script'):
            value = attributes.get('href','') if tag=='link' else attributes.get('src','')
            if value and not re.match(r'^(https?://|//|data:|#)', value):
                self.local_paths.append(value.split('#')[0].split('?')[0])

def main():
    page=(ROOT/'index.html').read_text(encoding='utf-8')
    p=SiteParser()
    p.feed(page)
    assert p.has_main and p.has_h1, 'Missing semantic main or h1'
    assert p.projects == 4, f'Expected 4 projects; found {p.projects}'
    assert not [a for a in p.anchors if a and a not in p.ids], 'Broken in-page anchor'
    assert not [a for a in p.local_paths if not (ROOT/a).is_file()], 'Missing local resource'
    assert (ROOT/'.nojekyll').is_file(), 'GitHub Pages build marker missing'
    js=(ROOT/'assets/site.js').read_text(encoding='utf-8')
    assert 'setLanguage' in js and '.dataset.filter' in js, 'Expected bilingual filters'
    for target in ('StockFlow','SuwoGym','data-quality-sales-inventory','Restaurante'):
        assert 'https://github.com/HenryGonzalezAlguera/'+target in page, f'Missing repo {target}'
    for target in ('/assets/favicon.svg','/assets/og-cover.png'):
        assert (ROOT/target.lstrip('/')).is_file()
    print('PASS: site structure, internal links, 4 projects, assets, translations and Pages marker')

if __name__=='__main__': main()