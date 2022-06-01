# Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup
engine = create_engine('sqlite:///hawaii.sqlite', echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup
app = Flask(__name__)


# Flask Routes
@app.route('/')
def homepage():
    return(
        f'Welcome!<br/>'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

@app.route('/api/v1.0/precipitation')
def precipitation():

    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    all_prcp = []
    for date, precip in results:
        prcp_dict = {}
        prcp_dict[date] = precip
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


@app.route('/api/v1.0/stations')
def stations():

    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

'''
@app.route('/api/v1.0/tobs')
def temperature():

    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).all()
    session.close()

    all_temps = []
    for date, temp in results:
        temp_dict = {}

    return jsonify()
    #return query results of 'date' and 'tobs' as dict
    #jsonify


@app.route('/api/v1.0/<start>')
def temp1():

    session = Session(engine)
    results = session.query().all()
    session.close()

@app.route('/api/v1.0/<start>/<end>')
def temp2():

    session = Session(engine)
    results = session.query().all()
    session.close()
'''

if __name__ == '__main__':
    app.run(debug=True)