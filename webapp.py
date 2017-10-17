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
        return render_template('gigaConversions.html')
    
@app.route("/yearToHour.html")
def render_years():
    if 'years' in request.args:
        years = float(request.args["years"])
        reply = years * 8766
        return render_template('yearToHour.html', response = reply)
    else: 
        return render_template('yearToHour.html')    

@app.route("/mileToKm.html")
def render_mile():
    if 'miles' in request.args:
        miles = float(request.args["miles"])
        reply = miles * 1.609       
        return render_template('mileToKm.html', response = reply)
    else: 
        return render_template('mileToKm.html')
if __name__=="__main__":
    app.run(debug=False, port=54321)
