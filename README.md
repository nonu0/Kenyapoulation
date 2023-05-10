# Kenyapoulation

Certainly! Here's the README file for the provided code:

# Population Data Visualization

This Django project provides data visualization for population statistics in different regions. It includes views for displaying population data for various regions such as Coast, Central, Nyanza, Rift Valley, Eastern, Northeastern, and Western.

## Prerequisites

Before running this project, ensure that you have the following installed:

- Python 3.x
- Django
- Django ORM
- SQLite (or any other compatible database)

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.

```bash
cd population-data-visualization
```

3. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
```

4. Activate the virtual environment.

- For Windows:

```bash
venv\Scripts\activate
```

- For Linux/macOS:

```bash
source venv/bin/activate
```

5. Install the project dependencies.

```bash
pip install -r requirements.txt
```

6. Apply the database migrations.

```bash
python manage.py migrate
```

## Usage

1. Start the development server.

```bash
python manage.py runserver
```

2. Open a web browser and visit [http://localhost:8000/](http://localhost:8000/) to access the home page.

## Views

### Home

- URL: /
- Template: home.html
- Context Variables:
  - `county_names`: List of county names.
  - `females_pop`: List of female populations for each county.
  - `males_pop`: List of male populations for each county.
  - `area`: List of areas for each county.
  - `females_sum`: Sum of all female populations.
  - `males_sum`: Sum of all male populations.

### Coast

- URL: /coast/
- Template: coast.html
- Context Variables:
  - `coast_counties`: List of county names in the Coast region.
  - `coast_females`: List of female populations for each county in the Coast region.
  - `coast_males`: List of male populations for each county in the Coast region.
  - `coast_area`: List of areas for each county in the Coast region.
  - `coast_females_sum`: Sum of female populations in the Coast region.
  - `coast_males_sum`: Sum of male populations in the Coast region.

### Central

- URL: /central/
- Template: central.html
- Context Variables:
  - `central_counties`: List of county names in the Central region.
  - `central_females`: List of female populations for each county in the Central region.
  - `central_males`: List of male populations for each county in the Central region.
  - `central_area`: List of areas for each county in the Central region.
  - `central_females_sum`: Sum of female populations in the Central region.
  - `central_males_sum`: Sum of male populations in the Central region.

### Nyanza

- URL: /nyanza/
- Template: nyanza.html
- Context Variables:
  - `nyanza_counties`: List of county names in the Nyanza region.
  - `nyanza_females`: List of female populations for each county in the Nyanza region.
  - `nyanza_males`: List of male populations for each county in the Nyanza region.
  - `nyanza_area`: List of areas for each county in the Nyanza region.
  - `nyanza_females_sum`: Sum of female populations in the Nyanza region.
  -`nyanza_males_sum`: Sum of male populations in the Nyanza region.

### Rift Valley

- URL: /rvalley/
- Template: rvalley.html
- Context Variables:
  - `rvalley_counties`: List of county names in the Rift Valley region.
  - `rvalley_females`: List of female populations for each county in the Rift Valley region.
  - `rvalley_males`: List of male populations for each county in the Rift Valley region.
  - `rvalley_area`: List of areas for each county in the Rift Valley region.
  - `rvalley_females_sum`: Sum of female populations in the Rift Valley region.
  - `rvalley_males_sum`: Sum of male populations in the Rift Valley region.

### Eastern

- URL: /eastern/
- Template: eastern.html
- Context Variables:
  - `eastern_counties`: List of county names in the Eastern region.
  - `eastern_females`: List of female populations for each county in the Eastern region.
  - `eastern_males`: List of male populations for each county in the Eastern region.
  - `eastern_area`: List of areas for each county in the Eastern region.
  - `eastern_females_sum`: Sum of female populations in the Eastern region.
  - `eastern_males_sum`: Sum of male populations in the Eastern region.

### Northeastern

- URL: /neastern/
- Template: neastern.html
- Context Variables:
  - `neastern_counties`: List of county names in the Northeastern region.
  - `neastern_females`: List of female populations for each county in the Northeastern region.
  - `neastern_males`: List of male populations for each county in the Northeastern region.
  - `neastern_area`: List of areas for each county in the Northeastern region.
  - `neastern_females_sum`: Sum of female populations in the Northeastern region.
  - `neastern_males_sum`: Sum of male populations in the Northeastern region.

### Western

- URL: /western/
- Template: western.html
- Context Variables:
  - `western_counties`: List of county names in the Western region.
  - `western_females`: List of female populations for each county in the Western region.
  - `western_males`: List of male populations for each county in the Western region.
  - `western_area`: List of areas for each county in the Western region.
  - `western_females_sum`: Sum of female populations in the Western region.
  - `western_males_sum`: Sum of male populations in the Western region.

## Contributing

If you would like to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

This project was developed as part of a data visualization exercise and is for educational purposes only. The population data used is from 2019 real-world statistics.
