import requests
import json

from flask import Flask, request, render_template


res = requests.get('https://yts.mx/api/v2/list_movies.json?sort_by=rating')
text = res.text
# print(type(text))

data = json.loads(text)
# print(type(data))

year_list = []

for i in range(0, len(data['data']['movies']) - 1):
    year_list.append(data['data']['movies'][i]['year'])

x = min(year_list)  # 1957
y = max(year_list)  # 2020

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_movies():
    if request.method == "GET":
        return render_template('index.html', uix=x, uiy=y)
    elif request.method == "POST":
        movies = []
        year = int(request.form['year'])
        for i in range(0, len(data['data']['movies']) - 1):
            if data['data']['movies'][i]['year'] == year:
                movies.append(data['data']['movies'][i]['title'])
                # datas = json.dumps(movies)
                datas = movies
        try:
            return render_template('index.html', uidata=datas, uix=x, uiy=y)
        except:
            return render_template('index.html', uidata="해당 연도의 영화를 찾을 수 없습니다.", uix=x, uiy=y)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
