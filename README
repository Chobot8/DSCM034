# Flask App Dockerized

## Description

This repository contains a Flask web application that serves a machine learning model for making predictions. The Flask app is Dockerized, making it easy to deploy and run in any environment.

## How to Use

1. **Clone Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to Project Directory:**
   ```bash
   cd <project-directory>
   ```

3. **Build Docker Image:**
   ```bash
   sudo docker build -t flask-app .
   ```

4. **Run Docker Container:**
   ```bash
   docker run -p 5000:5000 flask-app
   ```

5. **Test the Application:**
   Use `curl` to send a sample POST request to the Flask app:
   ```bash
   curl -X POST http://localhost:5000/predict \
   -H "Content-Type: application/json" \
   -d '{"data": [[8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23], [8.3014, 21, 6.238137, 1.072314, 240, 2.109842, 37.86, -122.22]]}'
   ```

   This command sends a JSON payload containing sample data to the `/predict` endpoint of the Flask app running on port 5000. Adjust the data as needed for your use case.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
