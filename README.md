# HouseHunt: Finding a Perfect Rental Home

A web application for finding rental houses with features like login, search by city/location, price range, number of bedrooms, 360° view, floor plan, price trends, save search, download results, and more.

## Features
- User login
- Search by city/location, price range, and number of bedrooms
- View available rent houses with images, floor plans, 360° tours, and Google Maps routes
- Save searches
- Download search results as CSV
- View price trends (sample chart)
- See real estate agents/brokers

## Setup Instructions
1. **Clone the repository or copy the files to your project directory.**
2. **Install dependencies:**
   ```sh
   python3 -m pip install -r requirements.txt
   python3 -m pip install fpdf
   ```
3. **Run the app:**
   ```sh
   python3 app.py
   ```
4. **Open your browser and go to:**
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
- **Login credentials:**
  - Username: `user`
  - Password: `pass`
- After login, search for rent houses, view results, save searches, download results, and more.

## Generate Project PDF
To generate a PDF with code and output description:
```sh
python3 generate_project_pdf.py
```

## File Structure
- `app.py` - Flask backend
- `templates/` - HTML templates
- `static/` - CSS files
- `requirements.txt` - Python dependencies
- `generate_project_pdf.py` - Script to generate project PDF
- `rent_house_finder_project.pdf` - Generated PDF (after running script)

## License
MIT 