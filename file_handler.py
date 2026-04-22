import zipfile

def extract_code(article):
    html_code = article.split('--html--')[1]
    css_code = article.split('--css--')[1]
    js_code = article.split('--js--')[1]
    return html_code, css_code, js_code

def save_files(html, css, js):
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

def create_zip():
    with zipfile.ZipFile('website.zip', 'w') as zipf:
        zipf.write('index.html')
        zipf.write('style.css')
        zipf.write('script.js')