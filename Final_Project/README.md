# News Sentiment Analysis

## Description
News Sentiment Analysis is a Python program that fetches news headlines from a news API, analyzes their sentiment using TextBlob, visualizes the sentiment distribution, and writes the headlines along with their sentiment and extra information to an Excel file.

## Requirements
- Python 3.x
- requests
- textblob
- matplotlib
- openpyxl
- pytest

## Installation
1. Clone the repository.
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the following command to start the application:
    ```
    python project.py
    ```
2. Enter a topic when prompted. The program will fetch news headlines related to the entered topic, analyze their sentiment, visualize the sentiment distribution, and save the data to an Excel file.

## Testing
To run tests, use:
```
pytest test_project.py
```

## Project Structure
```
final_project/
│
├── project.py
├── test_project.py
├── requirements.txt
└── README.md
```

## Contributors
- [Huzaifa Khan](https://github.com/botzaifa)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis.
- [matplotlib](https://matplotlib.org/) for data visualization.
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) for working with Excel files.
- [NewsAPI](https://newsapi.org/) for providing news headlines.
```

