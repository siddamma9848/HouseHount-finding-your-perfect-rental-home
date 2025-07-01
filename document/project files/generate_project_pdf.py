from fpdf import FPDF

# Read code files
with open('app.py', 'r') as f:
    app_code = f.read()
with open('templates/home.html', 'r') as f:
    home_html = f.read()
with open('templates/login.html', 'r') as f:
    login_html = f.read()
with open('static/style.css', 'r') as f:
    style_css = f.read()

description = '''\
HouseHunt: Finding a Perfect Rental Home
----------------------------------------
This project is a web application for finding rental houses. It features:
- User login
- Search by city/location, price range, and number of bedrooms
- View available rent houses with images, floor plans, 360° tours, and Google Maps routes
- Save searches
- Download search results as CSV
- View price trends (sample chart)
- See real estate agents/brokers

Sample Output:
--------------
After logging in, you can search for rent houses. Results are shown as cards with images, address, price, bedrooms, and links for 360° tour, floor plan, and Google Maps. You can save your search or download results as a CSV file.
'''

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'HouseHunt: Finding a Perfect Rental Home', ln=True, align='C')
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, description)

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'app.py', ln=True)
pdf.set_font('Courier', '', 9)
pdf.multi_cell(0, 4, app_code)

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'templates/home.html', ln=True)
pdf.set_font('Courier', '', 9)
pdf.multi_cell(0, 4, home_html)

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'templates/login.html', ln=True)
pdf.set_font('Courier', '', 9)
pdf.multi_cell(0, 4, login_html)

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'static/style.css', ln=True)
pdf.set_font('Courier', '', 9)
pdf.multi_cell(0, 4, style_css)

pdf.output('househunt_project.pdf')
print('PDF generated: househunt_project.pdf') 