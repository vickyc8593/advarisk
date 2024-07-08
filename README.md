# The Midnight Times

The Midnight Times is a Django web application that allows users to search for news articles, view previous searches, and refresh search results. The application leverages the News API to fetch news articles based on user-provided keywords.

## Features

- Search for news articles by keyword
- View a list of previous searches and their results
- Refresh search results to fetch the latest articles
- Sort search results based on the publication date
- Admin interface to manage users and block/unblock them

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8 or later
- Django 3.2 or later
- News API key (you can get one by signing up at [News API](https://newsapi.org/))

### Installation

1. **Clone the repository:**
    ```bash
    git clone (https://github.com/vickyc8593/advarisk)
    cd the-midnight-times
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Django settings:**
    - Create a `.env` file in the project root directory and add your News API key:
      ```env
      NEWS_API_KEY= "3278c0bf0b5541d1aa12cb5bc563de86"

      ```

5. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    - Open your browser and access the main application to `http://127.0.0.1:8000`.
    - Go to `http://127.0.0.1:8000/admin` to access the Django admin interface.

### File Structure

- `news/`
  - `admin.py` - Custom admin configurations.
  - `models.py` - Database models.
  - `urls.py` - URL configurations.
  - `views.py` - View functions.
  - `templates/news/` - HTML templates.
  - `static/news/` - Static files (CSS, JS).
  - `utils.py` - Utility functions for fetching news articles.
- `manage.py` - Django management script.
- `requirements.txt` - List of Python dependencies.
- `README.md` - Project documentation.

### Time Taken

- Initial setup and configuration: 2 hours
- Developing search functionality: 4 hours
- Implementing previous searches feature: 3 hours
- Adding refresh results functionality: 2 hours
- Designing frontend and integrating CSS: 4 hours
- Implementing admin features for user management: 3 hours
- Testing and debugging: 2 hours
- Documentation and README: 1 hour

**Total time: 21 hours**

### Overall Experience

Building The Midnight Times was a challenging yet rewarding experience. Integrating the News API and managing the front and backend data flow required careful planning and implementation. Enhancing the user interface to make it visually appealing involved learning and applying CSS techniques. Adding the functionality to refresh search results and preventing frequent searches for the same keyword improved the application's efficiency and user experience. Managing user permissions through the admin interface provided a deeper understanding of Django's admin capabilities. Overall, this project enhanced my skills in Django development, API integration, and frontend design.

### Future Improvements

- Implement user authentication to allow personalized searches.
- Add pagination for search results.
- Improve error handling and display user-friendly messages.
- Enhance the UI with more advanced CSS and JavaScript.

