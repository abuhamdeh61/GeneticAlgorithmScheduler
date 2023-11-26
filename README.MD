# Class Scheduling Application

This application uses Flask to create a web interface for generating class schedules using a Genetic Algorithm (GA). The scheduling logic is implemented in Python.

## Features

- **Genetic Algorithm Optimization:** The heart of the application lies in its Genetic Algorithm, intelligently crafting class schedules for maximum efficiency.
- **Web Interface with Flask:** A user-friendly web interface allows easy input of class details, and the GA backend seamlessly processes the data to generate optimal schedules.

- **Constraint Management:** The GA algorithm excels at handling constraints like maximum days, breaks, and courses, ensuring schedules adhere to specific requirements.

- **Flexible and Scalable:** Easily adaptable to different educational institutions, the application scales effortlessly to handle diverse scheduling scenarios.

- **Real-time Visualization:** Leverage the power of AJAX to dynamically update and visualize the generated schedules in real-time through an intuitive table interface. This feature enhances the user experience, providing seamless and instant feedback for effective review and analysis.

## Why Genetic Algorithms?

Genetic Algorithms offer a powerful solution for combinatorial optimization problems like class scheduling. By mimicking the principles of natural selection, GA efficiently explores the solution space, evolving towards optimal schedules. This approach excels in finding near-optimal solutions in complex and dynamic environments.

Explore the efficiency of Genetic Algorithms in revolutionizing class scheduling with this intelligent and adaptable Class Schedule Optimizer.

## Table of Contents

- [Web Interface](#web-interface)
- [Backend Logic](#backend-logic)
- [Folder Structure](#folder-structure)
- [How to Run](#how-to-run)

## Web Interface

The web interface is built using HTML templates with Flask. The main schedule input form is provided to add classes, and the generated schedules are displayed in a table. Users can submit the schedule, and the backend will process the data using a Genetic Algorithm.

### Technologies Used

- Flask
- Genetic Algorithm (GA)
- AJAX
- Bootstrap

## Backend Logic

The backend logic for class scheduling is implemented using a Genetic Algorithm (GA). The scheduling constraints, such as maximum days, maximum breaks, and maximum courses, are taken into account during the scheduling process.

### Genetic Algorithm Components

- Population Initialization
- Selection (Tournament Selection)
- Crossover
- Mutation

### Files

- `app.py`: Flask application file with routes for rendering the web interface and handling schedule generation.
- `course.py`: Class representing a course.
- `schedule.py`: Class representing a schedule with fitness calculation logic.
- `GA.py`: Genetic Algorithm implementation for schedule optimization.

## Folder Structure

- `templates`
  - `index.html`
  - `layout.html`
- `static`
  - `js`
  - `css`
- `app.py`
- `course.py`
- `schedule.py`
- `GA.py`
- `README.md`

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install Flask`.flask run
3. Run the Flask application by executing the command `flask run` in the terminal.
4. Open your web browser and navigate to `http://localhost:5000` to access the class scheduling application.
