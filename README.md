# VIT Chennai Login System

This is a Flask web application for the VIT Chennai login system with download links functionality.

## Features

1. Login page with conditional redirects:
   - If no email is entered, shows download links on the same page
   - If email is entered, redirects to the examly login page
2. System Compatibility Check page with download options presented as logos
3. Responsive design that works on different screen sizes

## Deployment to Vercel

1. Push this code to your GitHub repository
2. Connect your GitHub repository to Vercel
3. Vercel will automatically detect the Flask application and deploy it
4. The application will be accessible via a Vercel URL

## Local Development

To run the application locally:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Access the application at http://localhost:8000

## File Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: Static assets (CSS files)
- `requirements.txt`: Python dependencies
- `vercel.json`: Vercel deployment configuration