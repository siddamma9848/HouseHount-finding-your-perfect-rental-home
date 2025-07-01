from flask import Flask, render_template, request, redirect, url_for, session, send_file
import io
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Mock user
USER = {'username': 'user', 'password': 'pass'}

# Mock rental house data
HOUSES = [
    {'city': 'New York', 'price': 1200, 'address': '123 Main St, New York', 'bedrooms': 2, 'image_url': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80', 'map_query': '123 Main St, New York', 'floor_plan_url': 'https://www.houseplans.com/blog/wp-content/uploads/2017/09/plan-430-156-floor-plan.jpg', 'tour_360_url': 'https://kuula.co/share/7Yd7B?fs=1&vr=1&sd=1&thumbs=1&chromeless=1&logo=1'},
    {'city': 'Los Angeles', 'price': 1500, 'address': '456 Sunset Blvd, Los Angeles', 'bedrooms': 3, 'image_url': 'https://images.unsplash.com/photo-1460518451285-97b6aa326961?auto=format&fit=crop&w=400&q=80', 'map_query': '456 Sunset Blvd, Los Angeles', 'floor_plan_url': 'https://www.houseplans.com/blog/wp-content/uploads/2017/09/plan-430-156-floor-plan.jpg', 'tour_360_url': 'https://kuula.co/share/7Yd7B?fs=1&vr=1&sd=1&thumbs=1&chromeless=1&logo=1'},
    {'city': 'Chicago', 'price': 900, 'address': '789 Lake Shore Dr, Chicago', 'bedrooms': 1, 'image_url': 'https://images.unsplash.com/photo-1430285561322-7808604715df?auto=format&fit=crop&w=400&q=80', 'map_query': '789 Lake Shore Dr, Chicago', 'floor_plan_url': 'https://www.houseplans.com/blog/wp-content/uploads/2017/09/plan-430-156-floor-plan.jpg', 'tour_360_url': 'https://kuula.co/share/7Yd7B?fs=1&vr=1&sd=1&thumbs=1&chromeless=1&logo=1'},
    {'city': 'New York', 'price': 2000, 'address': '321 Broadway, New York', 'bedrooms': 4, 'image_url': 'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=400&q=80', 'map_query': '321 Broadway, New York', 'floor_plan_url': 'https://www.houseplans.com/blog/wp-content/uploads/2017/09/plan-430-156-floor-plan.jpg', 'tour_360_url': 'https://kuula.co/share/7Yd7B?fs=1&vr=1&sd=1&thumbs=1&chromeless=1&logo=1'},
    {'city': 'Los Angeles', 'price': 1100, 'address': '654 Hollywood Rd, Los Angeles', 'bedrooms': 2, 'image_url': 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80', 'map_query': '654 Hollywood Rd, Los Angeles', 'floor_plan_url': 'https://www.houseplans.com/blog/wp-content/uploads/2017/09/plan-430-156-floor-plan.jpg', 'tour_360_url': 'https://kuula.co/share/7Yd7B?fs=1&vr=1&sd=1&thumbs=1&chromeless=1&logo=1'},
]

AGENTS = [
    {'name': 'Alice Johnson', 'phone': '555-1234', 'email': 'alice@realestate.com'},
    {'name': 'Bob Smith', 'phone': '555-5678', 'email': 'bob@realestate.com'},
    {'name': 'Carol Lee', 'phone': '555-8765', 'email': 'carol@realestate.com'},
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    cities = sorted(set(h['city'] for h in HOUSES))
    bedrooms_options = sorted(set(h['bedrooms'] for h in HOUSES))
    results = HOUSES
    search_params = {}
    if request.method == 'POST':
        city = request.form['city']
        min_price = int(request.form['min_price'])
        max_price = int(request.form['max_price'])
        bedrooms = int(request.form['bedrooms'])
        results = [h for h in HOUSES if h['city'] == city and min_price <= h['price'] <= max_price and h['bedrooms'] == bedrooms]
        search_params = {'city': city, 'min_price': min_price, 'max_price': max_price, 'bedrooms': bedrooms}
    return render_template('home.html', cities=cities, bedrooms_options=bedrooms_options, results=results, search_params=search_params, agents=AGENTS)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/save_search', methods=['POST'])
def save_search():
    if 'user' not in session:
        return redirect(url_for('login'))
    search = request.form.to_dict()
    if 'saved_searches' not in session:
        session['saved_searches'] = []
    session['saved_searches'].append(search)
    session.modified = True
    return redirect(url_for('saved_searches'))

@app.route('/saved_searches')
def saved_searches():
    if 'user' not in session:
        return redirect(url_for('login'))
    searches = session.get('saved_searches', [])
    return render_template('saved_searches.html', searches=searches)

@app.route('/download_results', methods=['POST'])
def download_results():
    if 'user' not in session:
        return redirect(url_for('login'))
    city = request.form['city']
    min_price = int(request.form['min_price'])
    max_price = int(request.form['max_price'])
    bedrooms = int(request.form['bedrooms'])
    results = [h for h in HOUSES if h['city'] == city and min_price <= h['price'] <= max_price and h['bedrooms'] == bedrooms]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Address', 'City', 'Price', 'Bedrooms'])
    for h in results:
        writer.writerow([h['address'], h['city'], h['price'], h['bedrooms']])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='rent_houses.csv')

if __name__ == '__main__':
    app.run(debug=True) 