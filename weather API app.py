# WEATHER API PROGRAM   (LAST ONE FROM BRO CODE)


import sys
from wsgiref.util import application_uri
import requests

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


# 5fe60d5f637dd307eb03dc293c117a82

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("Weather app", self)
        self.weather_label = QLabel("Enter your city name ", self)
        self.weather_textbox = QLineEdit(self)
        self.weather_button = QPushButton("Get weather", self)
        self.temp_label = QLabel(self)
        self.description_weather = QLabel(self)
        self.emoji_label = QLabel(self)

        self.init()

    def init(self):
        self.setWindowIcon(QIcon("william-warby-VwqMTcsb0Tg-unsplash.jpg"))
        self.setWindowTitle("Weather app")
        self.setGeometry(570, 300, 800, 500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.weather_textbox)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.description_weather)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)

        self.setLayout(vbox)

        self.title_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weather_textbox.setAlignment(Qt.AlignCenter)
        self.description_weather.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.title_label.setObjectName("title_label")
        self.weather_label.setObjectName("weather_label")
        self.weather_textbox.setObjectName("weather_textbox")
        self.weather_button.setObjectName("weather_button")
        self.description_weather.setObjectName("description_weather")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")

        self.setStyleSheet("""
        QLabel,QPushButton{
        font-family:calibri;
        font-style:italic;
        }
        QLabel#title_label{
        font-size:70px;
        font-weight:bold;
        }
        QLabel#weather_label{
        font-size:35px;
        }
        QLineEdit#weather_textbox{
        font-size:30px;
        padding:15px;  
        }
        QPushButton#weather_button{
        font-size:25px;
        padding:15px;
        }
        QLabel#description_weather{
        font-size:50px;
        }
        QLabel#temp_label{
         font-size:50px;
        }
        QLabel#emoji_label{
        font-size:100px;
        }

                """)

        self.weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        try:
            api = "5fe60d5f637dd307eb03dc293c117a82"
            city = self.weather_textbox.text()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:

            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error("Internal server error\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway\nInvalid response frm the server")
                case 503:
                    self.display_error("Server unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway timeout\npNo response from server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")


        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nConnection is lost")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error\n{req_error}")

    def display_error(self, message):

        self.description_weather.setText(message)
        self.emoji_label.clear()
        self.temp_label.clear()

    def display_weather(self, data):
        temp_value = data["main"]["temp"]
        self.description_weather.setText(f"{temp_value:.0f} Degrees Celsius ")

        temp_description = data["weather"][0]["description"]
        self.temp_label.setText(f"{temp_description}")

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.emoji_weatherapp(weather_id))

    @staticmethod
    def emoji_weatherapp(weather_id):

        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif weather_id >= 100 and weather_id <= 321:
            return "⛅"
        elif weather_id >= 500 and weather_id <= 531:
            return "🌧️"
        elif weather_id >= 600 and weather_id <= 622:
            return "🌨️"
        elif weather_id >= 701 and weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id >= 801 and weather_id <= 804:
            return "☁️"
        else:
            return ""


def main():
    app = QApplication(sys.argv)
    weathapp = WeatherApp()
    weathapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
