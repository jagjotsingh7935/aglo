# To-Do List App (Backend)

A Django-based backend for a To-Do List application, developed as part of a coding assignment for the AlgoBulls Backend Developer Internship (Full-Time) - November 2024.

## Features

- **Task Management:** CRUD operations for To-Do items.
- **Tag Support:** Add and manage tags for tasks.
- **Authentication:** Secure APIs with Basic Authentication.
- **Status Updates:** Track task statuses such as Open, Working, Completed, etc.
- **RESTful APIs:** Built using Django Rest Framework (DRF).
- **Admin Interface:** Comprehensive admin panel with validations and filters.

## Demo

[Add a link to your hosted application here.]

### Screenshots

![Screenshot 1]![image1](https://github.com/user-attachments/assets/a8f94b09-1948-4a67-97cc-e4601b9cb17e)

![Screenshot 2]![{723F5BD7-3AD3-4A05-AEAD-DEB94C0A5B34}](https://github.com/user-attachments/assets/a568dcd7-b631-420c-ba69-dc420905c65e)

![Screenshot 3]! ![{184D2C70-B2C5-49A4-B8FF-2428484840D5}](https://github.com/user-attachments/assets/d337c7b0-f5d7-4b9c-a75c-a5da9aa4c5c2)



(Add more images as needed.)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-backend.git
   cd todo-list-backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

[Link to your hosted API documentation.]

## Running Tests

1. Unit and Integration Tests:
   ```bash
   python manage.py test
   ```

2. Coverage Report:
   - View coverage summary:
     ```bash
     coverage run --source='.' manage.py test && coverage report
     ```
   - Generate HTML coverage report:
     ```bash
     coverage html
     ```

3. End-to-End (E2E) Tests:
   Use Selenium for E2E testing. Refer to the [E2E Testing Documentation](https://docs.djangoproject.com/en/4.2/topics/testing/) for detailed instructions.

## CI/CD

This project includes GitHub Actions for:
- Running unit, integration, and E2E tests.
- Code linting using Flake8 and formatting with Black.


##Postman

![Screenshot 1] ![{DD3CF687-8342-414E-824F-EA4ADEC6DD22}](https://github.com/user-attachments/assets/85b6e536-78a9-426a-9711-619b4487440c)
![Screenshot 2] ![{CF9E78E2-0587-4ED5-97F3-D16FAB46C4EC}](https://github.com/user-attachments/assets/341de69b-1853-4ee9-a5f0-e986c0eec88a)


## Deliverables

- **Hosted App Link:** [Add your cloud-hosted app link here.]
- **Postman Collection Link:** [Add the Postman Collection link here.]
- **Admin Credentials:** (Share privately as instructed.)
- **Documentation:** [Add a link to the hosted static site documentation here.]

## Technology Stack

- **Backend Framework:** Django 4.2.7+
- **Programming Language:** Python 3.11+
- **REST Framework:** Django Rest Framework 3.14.0+
- **Testing Tools:** Django Test Framework, Selenium
- **Linting and Formatting:** Flake8, Black

## Coverage Report

![Coverage Screenshot]![image](https://github.com/user-attachments/assets/36029d8f-51a8-4ad3-9c22-8a94070a030d)


## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
