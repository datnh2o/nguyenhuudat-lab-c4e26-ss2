from flask import Flask, render_template, request
app = Flask(__name__)

ex1 = [
    {
        "Model": "Honda" ,
        "Daily fee (VND)": 100000 ,
        "Image": "https://hondaxemay.com.vn/" ,
        "Year": 2013
    },
]

@app.route("/new_bike", methods = ["GET", "POST"])
def ex1():
    if request.method == "GET":
        return render_template("ex1.html", ) 
    elif request.method == "POST":
        form = request.form
        m = form["Model"]
        d = form["Daily fee (VND)"]
        i = form["Image"]
        y = form["Year"]

        new_item = {
                "Model": m,
                "Daily fee (VND)": d,
                "Image": i,
                "Year": y
            }
    ex1.append(new_item)
    return str(ex1)



if __name__ == '__main__':
  app.run(debug=True)