# Square Calculator

This is a simple web application that calculates the square of a number.

## Requirements

- Python 3
- Flask

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd square-calculator
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**

    ```bash
    python main.py
    ```

4.  Open your browser and go to `http://127.0.0.1:5000`

## Docker

To run the application with Docker:

1.  **Build the Docker image:**

    ```bash
    docker build -t square-calculator .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 square-calculator
    ```

## Testing

To run the unit tests:

```bash
python test_main.py
```