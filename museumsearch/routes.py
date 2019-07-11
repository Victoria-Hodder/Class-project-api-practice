from flask import Flask, jsonify, render_template, url_for, request
from museumsearch import app
from run import cur

@app.route('/')
def get_index():
    cur.execute(query)
    row = cur.fetchone()
    rows = cur.fetchall()
    print(rows)
    return render_template('index.html', exhibits=rows)


@app.route('/search')
def get_search_results():
    results = []
    searchterm = request.args.get('query')
    #import pdb; pdb.set_trace()
    if searchterm:
        for exhibit in rows:
            if exhibit['keyword'] == searchterm:
                results.append(exhibit)
    else:
        results = rows
    return render_template('search.html', results=results)
