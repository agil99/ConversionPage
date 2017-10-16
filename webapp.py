from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/gigaConversions.html")
def render_giga():
    if 'giga' in request.args:
        gigaAmount = float(request.args["giga"])
        reply = gigaAmount * 2000000000       
        return render_template('gigaConversions.html', response = reply)
    else: 
        return render_templat('gigaConversions.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
