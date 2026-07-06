# 🎵 Spotify Data Studio

A modular Python application for loading, cleaning, analyzing, and visualizing Spotify music datasets using Object-Oriented Programming (OOP) principles and common Data Science techniques.

---

## 📖 Overview

Spotify Data Studio is designed to provide a complete workflow for working with Spotify track data.

The project demonstrates how to build a maintainable data analysis application by separating responsibilities into independent modules. It supports data loading, preprocessing, statistical analysis, visualization, and interactive dataset management.

The application follows clean software design principles, making it easy to extend with new cleaning strategies, analysis methods, or visualizations.

---

## ✨ Features

### 📂 Dataset Management

* Load Spotify datasets from CSV files
* Add new songs interactively
* Save new records directly to the dataset
* Convert CSV data into Python objects

### 🧹 Data Cleaning

* Missing Value Handling

  * Mean Imputation
  * Median Imputation
  * K-Nearest Neighbors (KNN) Imputation

* Outlier Detection

  * Z-Score Method
  * Interquartile Range (IQR) Method

* Outliers are converted to **NaN** before imputation, preserving the original observations instead of removing entire rows.

---

### 📊 Data Analysis

The project provides several analytical utilities, including:

* Dataset summary
* Descriptive statistics
* Missing value report
* Duplicate detection
* Correlation matrix
* Genre insights
* Artist insights
* Most popular tracks
* Most popular track for each genre
* Average popularity by genre
* Feature distribution analysis

---

### 📈 Data Visualization

Supported visualizations include:

* Histogram
* Box Plot
* Scatter Plot
* Correlation Heatmap
* Genre Distribution
* Artist Distribution
* Average Popularity by Genre
* Radar Chart for Audio Features

---

## 🏗️ Project Structure

```text
spotify-data-studio/
│
├── data/
│   └── spotify_tracks.csv
│
├── src/
│   ├── analyzers/
│   ├── cleaners/
│   ├── visualizers/
│   ├── models/
│   ├── loaders/
│   ├── utils/
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Project Architecture

The application is built around the **Single Responsibility Principle (SRP)**.

Each module has one clear responsibility:

| Module         | Responsibility             |
| -------------- | -------------------------- |
| DataLoader     | Read and write CSV files   |
| Song           | Represents a Spotify track |
| DataCleaner    | Data preprocessing         |
| DataAnalyzer   | Statistical analysis       |
| DataVisualizer | Data visualization         |

Cleaning strategies are implemented using the **Strategy Design Pattern**, allowing different preprocessing techniques to be swapped without changing the main application.

---

## 🛠️ Technologies

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/spotify-data-studio.git
```

Move into the project directory:

```bash
cd spotify-data-studio
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the application using:

```bash
python main.py
```

The program provides an interactive command-line interface where you can:

* Load datasets
* Clean data
* Perform analysis
* Generate visualizations
* Add new songs
* Save changes

---

## 📊 Example Workflow

```text
Load Dataset
      │
      ▼
Clean Missing Values
      │
      ▼
Detect Outliers
      │
      ▼
Replace Outliers with NaN
      │
      ▼
Apply Imputation
      │
      ▼
Analyze Dataset
      │
      ▼
Generate Visualizations
```

---

## 🎯 Educational Objectives

This project demonstrates practical applications of:

* Object-Oriented Programming (OOP)
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Statistical Analysis
* Data Visualization
* Strategy Design Pattern
* CSV File Processing
* Scientific Python Libraries

---

## 📌 Future Improvements

Possible future extensions include:

* Export analytical reports
* Interactive dashboard
* Machine Learning models
* Music recommendation system
* SQL database integration
* REST API
* GUI version
* Unit testing

---

## 🤝 Contributing

Contributions are welcome.

If you have ideas for improvements or new analysis methods, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is intended for educational purposes.
