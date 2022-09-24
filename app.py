from flask import Flask
from flask import render_template
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
            "무용" : "/contents/dance",
            "국악" : "/contents/kor",
            "연극" : "/contents/play"
    }
    other_cats = {"기간별" : "/period",
            "지역별" : "/location"
    }
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)

@app.route('/contents/<condition>')
def contents_value(condition):
    menus = {"뮤지컬" : "/contents/musical",
            "클래식" : "/contents/classic",
            "무용" : "/contents/dance",
            "국악" : "/contents/kor",
            "연극" : "/contents/play"
    }
    other_cats = {"기간별" : "/period",
            "지역별" : "/location"
    }
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['genrenm'] == fil]
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))

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
    other_cats = {"기간별" : "/period",
            "주제별" : "/contents",
        }
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)

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
    other_cats = {"기간별" : "/period",
            "주제별" : "/contents"
    }
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['SGG'] == fil]
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))

@app.route('/period')
def period():
    menus = {"공연중" : "/period/on",
            "공연예정" : "/period/plan",
        }
    other_cats = {"지역별" : "/location",
            "주제별" : "/contents",
        }
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=None)

@app.route('/period/<condition>')
def period_value(condition):
    menus = {"공연중" : "/period/on",
            "공연예정" : "/period/plan",
        }
    other_cats = {"지역별" : "/location",
            "주제별" : "/contents"
    }
    for k, v in menus.items():
        if v.split('/')[-1] == condition:
            fil = k
    contents = data[data['prfstate'] == fil]
    return render_template('main.html', menu=menus, other_cats=other_cats, condition=condition, contents=contents.to_dict('records'))


@app.route('/item/<id>')
def view_item(id):
    contents = data[data['mt20id'] == id]

    return render_template('item.html', contents=contents.to_dict('records')[0])


if __name__=="__main__":
    global data
    data = pd.read_csv('data.csv')
    app.run()