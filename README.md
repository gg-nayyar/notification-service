# Notification System

A notification system built with FastAPI, Celery, and Uvicorn. It supports sending notifications via email and SMS and in app notifications.

---

## Features
- REST API for sending notifications
- Asynchronous task processing with Celery(RabbitMQ)
- Email and SMS notification services
- Uvicorn for production server
- Can now send mails to multiple emails

> **Note:** The SMS service will work for registered mobile numbers only, as it is a paid service. To register your number for testing, please email: krishsenpai7@gmail.com

---

## Project Structure
```
notification_system/
├── app/
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── task.py
│   └── services/
│       ├── email_service.py
│       └── sms_service.py
├── worker.py
├── start.sh
├── requirement.txt
├── ReadMe.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Redis (for Celery broker)

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd notification_system
   ```
2. Install dependencies:
   ```sh
   pip install -r requirement.txt
   ```

### Running the Application Locally

1. **Start Redis Server**
   - Make sure Redis is running locally or update Celery config for your broker.
2. **Start Celery Worker**
   ```sh
   celery -A worker.celery worker --loglevel=info
   ```
3. **Start the API Server**
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000` when running locally.

---

## Deployment

This project is already deployed on Render using Uvicorn. You can access the live API and Swagger docs at:

[Live Swagger UI](https://notification-service-api.onrender.com/docs)

---

## API Endpoints

| Method | Route                           | Description                                 |
|--------|----------------------------------|---------------------------------------------|
| POST   | /notifications                  | Send a notification (email or SMS or inapp)          |
| GET    | /users/{user_id}/notifications  | Get all notifications for a specific user   |

---

**Note** Make Sure to check your spam folder.

## Example Input/Output

### Input Inapp Messages Example

![Input Example](https://github.com/gg-nayyar/notification-service/blob/main/Post%20request.png)

### Output Inapp Messages Example

![Output Example](https://github.com/gg-nayyar/notification-service/blob/main/Post%20response.png)

### Input Email Example

![Input Example](https://github.com/gg-nayyar/notification-service/blob/main/email%20post.png)

### Output Email Example

![Output Example 1](https://github.com/gg-nayyar/notification-service/blob/main/email%20response.png)

![Output Example 2](https://github.com/gg-nayyar/notification-service/blob/main/mail%20example.jpg)

### Input SMS Example

![Input Example](https://github.com/gg-nayyar/notification-service/blob/main/sms%20post.png)

### Output SMS Example

![Output Example 1](https://github.com/gg-nayyar/notification-service/blob/main/sms%20response.png)

!![Output Example 2](https://github.com/gg-nayyar/notification-service/blob/main/twilio%20example.jpg)

### GET User Request

![Input Example](https://github.com/gg-nayyar/notification-service/blob/main/Get%20request.png)

### GET User Response

!![Output Example](https://github.com/gg-nayyar/notification-service/blob/main/get%20response.png)

---

## API Documentation

Interactive API docs are available at:

[Swagger UI](https://notification-service-api.onrender.com/docs)

---

## License
MIT
