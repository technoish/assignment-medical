# Django Multi-User Authentication System

A Django web application that provides role-based authentication for **Patients** and **Doctors** with separate dashboards and comprehensive user management features.

## Features

- **Multi-User Registration**: Separate registration for Patients and Doctors
- **Role-Based Authentication**: Different login experiences based on user type
- **Comprehensive User Profiles**: Complete user information with profile pictures
- **Responsive Design**: Bootstrap-powered mobile-friendly interface
- **Dashboard System**: Customized dashboards for each user type
- **Address Management**: Full address fields with validation
- **Profile Picture Upload**: Image upload with fallback display
- **Password Security**: Configurable password validation

## Requirements

- Python 3.9+
- Django 4.0+
- Pillow (for image handling)


### Project Structure

Create the following directory structure:

```
assignment-medical/
├── cms/
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── account/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       └── accounts/
│           ├── base.html
│           ├── signup.html
│           ├── login.html
│           ├── patient_dashboard.html
│           └── doctor_dashboard.html
├── media/
│   └── profile_pics/
├── README.md
├── requirement.txt
└── manage.py
```
### Create Virtual Environment
```bash
python -m venv .env
```

### Activate Virtual Environment
Windows:
```bash
 .env/Scripts/activate
```
### Install Requirements
```bash
 pip install -r requirement.txt
```

### Run Development Server

```bash
python manage.py runserver
```

## Usage

### User Registration

1. Navigate to `http://127.0.0.1:8000/signup/`
2. Fill in the registration form with:
   - **Personal Info**: First name, last name, username
   - **User Type**: Select Patient or Doctor
   - **Contact**: Email address
   - **Profile Picture**: Upload image (optional)
   - **Address**: Complete address details
   - **Security**: Password and confirmation

### User Login

1. Go to `http://127.0.0.1:8000/login/`
2. Enter username and password
3. System automatically redirects to appropriate dashboard

### Dashboards

- **Patient Dashboard**: `http://127.0.0.1:8000/patient/dashboard/`
- **Doctor Dashboard**: `http://127.0.0.1:8000/doctor/dashboard/`

Each dashboard displays:
- User profile information
- Profile picture or default avatar
- Complete address details
- Role-specific action buttons
- Account information


### Styling

The application uses Bootstrap 5. To customize:

1. Modify CSS in `base.html`
2. Update Bootstrap classes in templates
3. Add custom CSS files

## File Structure Details

### Core Files

- **`models.py`**: Custom User model extending AbstractUser
- **`forms.py`**: Registration and login forms with validation
- **`views.py`**: View functions for auth and dashboards
- **`urls.py`**: URL routing configuration
- **`admin.py`**: Admin interface customization

### Templates

- **`base.html`**: Base template with navigation and styling
- **`signup.html`**: User registration form
- **`login.html`**: User login form
- **`patient_dashboard.html`**: Patient-specific dashboard
- **`doctor_dashboard.html`**: Doctor-specific dashboard

## Security Features

- **Role-Based Access Control**: Users can only access their designated dashboards
- **Password Validation**: Configurable password strength requirements
- **CSRF Protection**: Built-in Django CSRF protection
- **User Authentication**: Secure login/logout functionality
- **Profile Picture Security**: Secure file upload handling

### Access Control Testing

1. Login as patient → should redirect to patient dashboard
2. Login as doctor → should redirect to doctor dashboard
3. Try accessing wrong dashboard → should show access denied

## Troubleshooting

### Common Issues

1. **"This password is too common" error**
   - Use stronger passwords like `MySecure@Pass123`
   - Or disable password validation in settings

2. **Media files not displaying**
   - Ensure `MEDIA_URL` and `MEDIA_ROOT` are set
   - Add media URL patterns to main `urls.py`

3. **Template not found errors**
   - Check template directory structure
   - Ensure app is in `INSTALLED_APPS`

4. **Migration errors**
   - Delete migration files and recreate
   - Ensure `AUTH_USER_MODEL` is set before first migration

## License

This project is open source and available under the MIT License.
