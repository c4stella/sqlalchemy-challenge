# Flask Setup
from flask import Flask, jsonify

app = Flask(__name__)


# Flask Routes
@app.route('/')
def homepage():
    return(
        f'Welcome!<br/>'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation'
        f'/api/v1.0/stations'
        f'/api/v1.0/tobs'
        f'/api/v1.0/<start>'
        f'/api/v1.0/<start>/<end>'
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    return jsonify()
    #return query results of 'date' and 'prcp' as dict
    #jsonify


@app.route('/api/v1.0/stations')
def stations():
    return jsonify()
    #return list of stations
    #jsonify


@app.route('/api/v1.0/tobs')
def temperature():
    return jsonify()
    #return query results of 'date' and 'tobs' ast dict
    #jsonify


@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')


if __name__ == "__main__":
    app.run(debug=True)