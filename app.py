# from urllib import request
from flask import Flask
from flask import render_template, request
from flask import redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('contents'))

@app.route('/contents')
def contents():
    menus = {"뮤지컬" : "/contents/musical",
            "클래식" : "/contents/classic",
            "오페라" : "/contents/opera",
            "무용" : "/contents/dance",
            "연극" : "/contents/play",
            "국악" : "/contents/kor",
    }
    
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=None, contents=data.to_dict('records'))

@app.route('/contents/<condition>')
def contents_value(condition):
    menus = {"뮤지컬" : "/contents/musical",
            "클래식" : "/contents/classic",
            "오페라" : "/contents/opera",
            "무용" : "/contents/dance",
            "연극" : "/contents/play",
            "국악" : "/contents/kor",
    }
    
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['genrenm'] == fil]
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))

@app.route('/location')
def location():
    menus = {"중구" : "/location/jung",
            "수성구" : "/location/su",
            "달서구" : "/location/dal",
            "북구" : "/location/buk",
            "남구" : "/location/nam",
            "동구" : "/location/dong",
            "서구" : "/location/seo",
            "달성군" : "/location/dals",
        }
    
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=None, contents=data.to_dict('records'))

@app.route('/location/<condition>')
def location_value(condition):
    menus = {"중구" : "/location/jung",
            "수성구" : "/location/su",
            "달서구" : "/location/dal",
            "북구" : "/location/buk",
            "남구" : "/location/nam",
            "동구" : "/location/dong",
            "서구" : "/location/seo",
            "달성군" : "/location/dals",
        }
    
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['SGG'] == fil]
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))

@app.route('/period')
def period():
    menus = {"공연중" : "/period/on",
            "공연예정" : "/period/plan",
        }
    
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=None, contents=data.to_dict('records'))

@app.route('/period/<condition>')
def period_value(condition):
    menus = {"공연중" : "/period/on",
            "공연예정" : "/period/plan",
        }
    
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['prfstate'] == fil]
    # return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))
    return render_template('index.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))


@app.route('/item/<id>')
def view_item(id):
    contents = data[data['mt20id'] == id]

    # return render_template('item.html', contents=contents.to_dict('records')[0])
    return render_template('info.html', contents=contents.to_dict('records')[0])

@app.route('/search', methods=['GET', 'POST'])
def search_keyword():
    condition = None
    menus = {"공연중" : "/period/on",
            "공연예정" : "/period/plan",
        }
    if request.method == 'POST':
        keyword = request.form['keyword']
        contents = data[data['prfnm'].str.contains(keyword)]
        return render_template('index.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))
    else:
        return "Something got wrong, Try again"

if __name__=="__main__":
    global data
    global other_cats
    data = pd.read_csv('data.csv')
    other_cats = {"지역별" : "/location",
            "주제별" : "/contents",
            "기간별" : '/period',
    }
    app.run(host="0.0.0.0", port=7750)