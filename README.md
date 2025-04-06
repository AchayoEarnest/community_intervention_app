# Community Intervention App

## Overview

The Community Intervention App is a Django-based web application designed to track and manage community interventions for enrolled Adolescent and Young People (AYP). The system allows users to enroll community members, record interventions, and monitor progress.

## Features

- User Authentication: Secure login and registration system.
- Enrollment Management: Add and track enrolled individuals.
- Intervention Tracking: Record interventions with timestamps.
- Search & Filtering: Easily find enrollments and interventions.
- User-Friendly Interface: Simple and intuitive design.

## Technologies Used

- Backend: Django, Django REST Framework
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite3
- Authentication: Django Authentication System

## Installation

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Django 4+
- SQLite3
- Virtual environment

## Setup

1. Clone the Repository
2. git clone https://github.com/AchayoEarnest/community_intervention_app.git
   cd community-intervention-app
3. Create a Virtual Environment
4. python -m venv venv

```sh
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

5. Install Dependencies

```sh
   pip install -r requirements.txt
```

6. Set Up the Database

```sh
   python manage.py migrate
```

7. Create a Superuser

```sh
   python manage.py createsuperuser
```

8. Run the Development Server

```sh
   python manage.py runserver
```

- Access the app at http://127.0.0.1:8000/ or https://community-interventio-app-09c22f89f155.herokuapp.com/ 
  Usage
  User Registration & Login
- Users can sign up and log in to access the dashboard.
  Enrolling Community Members
- Navigate to Enrollments → Add Enrollment to register a new individual.
  Recording Interventions
- Select an enrolled individual and add an intervention record.
  Viewing Reports
- Administrators can filter and view interventions by date, category, or user.

## API Endpoints

## Method Endpoint Description

GET /enrollment-list-api/ Get all enrollments
POST /enrollment-create/ Create a new enrollment
GET /api/interventions/ Get all interventions
POST /api/interventions/ Record a new intervention

## Future Enhancements

- Export reports as XLS/CSV
- SMS/Email notifications for interventions
- Advanced analytics dashboard

## Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, reach out at earnytech@live.com or open an issue on GitHub.
