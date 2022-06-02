# Dependencies
import numpy as np
import datetime as dt

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

@app.route('/api/v1.0/tobs')
def temperature():

    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
        filter((Measurement.date <= '2017-08-23') & (Measurement.date >= '2016-08-23')).all()
    session.close()

    all_temps = list(np.ravel(results))

    return jsonify(all_temps)

@app.route('/api/v1.0/<start>')
def start(startdate):

    startdate = dt.date.strftime('%Y%m%d')

    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= startdate).all()
    session.close()

    st_temp = list(np.ravel(results))
    return jsonify(st_temp)


@app.route('/api/v1.0/<start>/<end>')
def startend(startdate, enddate):

    startdate = dt.date.strftime('%Y%m%d')
    enddate = dt.date.strftime('%Y%m%d')

    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter((Measurement.date >= startdate) & (Measurement.date <= enddate)).all()
    session.close()

    sted_temp = list(np.ravel(results))
    return jsonify(sted_temp)


if __name__ == '__main__':
    app.run(debug=True)