import redis
import flask

print("starting")
app = flask.Flask(__name__)
r = redis.Redis(host='localhost', port=36379, db=0)

@app.route('/count')
def count():
    r.incr('hits')
    return 'This page has been viewed %s times.' % r.get('hits')

app.run(host='0.0.0.0', port=3000)
