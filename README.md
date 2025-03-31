# Community Intervention App

#Overview
The Community Intervention App is a Django-based web application designed to track and manage community interventions for enrolled Adolescent and Young People(AYP). The system allows users to enroll community members, record interventions, and monitor progress.
Features
• User Authentication: Secure login and registration system.
• Enrollment Management: Add and track enrolled individuals.
• Intervention Tracking: Record interventions with timestamps.
• Role-Based Access: Assign different permissions to users.
• Search & Filtering: Easily find enrollments and interventions.
• User-Friendly Interface: Simple and intuitive design.
#Technologies Used
• Backend: Django, Django REST Framework
• Frontend: HTML, CSS, Bootstrap
• Database: SQLite
• Authentication: Django Authentication System

#Installation
Prerequisites
Ensure you have the following installed:
• Python 3.8+
• Django 4+
• Sqlite3
• Virtual environment
#Setup

1. Clone the Repository
2. git clone https://github.com/yourusername/community-intervention-app.git
   cd community-intervention-app
3. Create a Virtual Environment
4. python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
5. Install Dependencies
   pip install -r requirements.txt
6. Set Up the Database
   python manage.py migrate
7. Create a Superuser
   python manage.py createsuperuser
8. Run the Development Server
   python manage.py runserver
   Access the app at http://127.0.0.1:8000/
   Usage
9. User Registration & Login
   • Users can sign up and log in to access the dashboard.
10. Enrolling Community Members
    • Navigate to Enrollments → Add Enrollment to register a new individual.
11. Recording Interventions
    • Select an enrolled individual and add an intervention record.
12. Viewing Reports
    • Administrators can filter and view interventions by date, category, or user.
    API Endpoints
    Method Endpoint Description
    GET /api/enrollments/ Get all enrollments
    POST /api/enrollments/ Create a new enrollment
    GET /api/interventions/ Get all interventions
    POST /api/interventions/ Record a new intervention
    #Future Enhancements
    • Export reports as XLS/CSV
    • SMS/Email notifications for interventions
    • Advanced analytics dashboard
    Contributing
    Contributions are welcome! Feel free to fork the repo and submit pull requests.
    License
    This project is licensed under the MIT License.
    Contact
    For questions or support, reach out at [earnytech@live.com] or open an issue on GitHub.