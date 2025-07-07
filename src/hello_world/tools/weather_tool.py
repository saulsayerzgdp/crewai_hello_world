from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Any

class WeatherForecastInput(BaseModel):
    day: str = Field(..., description="Day of the week for the weather forecast (e.g., 'Monday')")

class WeatherForecastTool(BaseTool):
    name: str = "weather_forecast_tool"
    description: str = "Gets weather forecast for a specified day for all supported locations."
    args_schema: type[BaseModel] = WeatherForecastInput

    _weather_data = {
        "New York": {
            "Monday": {"condition": "Sunny", "temperature": 25, "humidity": 60},
            "Tuesday": {"condition": "Partly Cloudy", "temperature": 23, "humidity": 65},
            "Wednesday": {"condition": "Cloudy", "temperature": 22, "humidity": 70},
            "Thursday": {"condition": "Rainy", "temperature": 20, "humidity": 80},
            "Friday": {"condition": "Thunderstorm", "temperature": 19, "humidity": 85},
            "Saturday": {"condition": "Cloudy", "temperature": 21, "humidity": 75},
            "Sunday": {"condition": "Sunny", "temperature": 24, "humidity": 65}
        },
        "London": {
            "Monday": {"condition": "Rainy", "temperature": 18, "humidity": 75},
            "Tuesday": {"condition": "Cloudy", "temperature": 17, "humidity": 70},
            "Wednesday": {"condition": "Partly Cloudy", "temperature": 19, "humidity": 65},
            "Thursday": {"condition": "Sunny", "temperature": 21, "humidity": 60},
            "Friday": {"condition": "Partly Cloudy", "temperature": 20, "humidity": 65},
            "Saturday": {"condition": "Cloudy", "temperature": 18, "humidity": 70},
            "Sunday": {"condition": "Rainy", "temperature": 17, "humidity": 75}
        },
        "Tokyo": {
            "Monday": {"condition": "Sunny", "temperature": 28, "humidity": 55},
            "Tuesday": {"condition": "Sunny", "temperature": 29, "humidity": 50},
            "Wednesday": {"condition": "Partly Cloudy", "temperature": 27, "humidity": 60},
            "Thursday": {"condition": "Cloudy", "temperature": 26, "humidity": 65},
            "Friday": {"condition": "Rainy", "temperature": 24, "humidity": 75},
            "Saturday": {"condition": "Thunderstorm", "temperature": 23, "humidity": 80},
            "Sunday": {"condition": "Cloudy", "temperature": 25, "humidity": 70}
        }
    }

    def _run(self, day: str, **kwargs: Any) -> str:
        try:
            day = day.capitalize()
            locations = list(self._weather_data.keys())
            forecast = f"Weather forecast for {day}:\n\n"
            for location in locations:
                day_data = self._weather_data[location].get(day)
                if not day_data:
                    forecast += f"{location}: No data available.\n"
                    continue
                temp = day_data["temperature"]
                forecast += f"{location}: {day_data['condition']}, {temp}°C, Humidity: {day_data['humidity']}%\n"
            return forecast
        except Exception as e:
            return f"Error providing weather forecast: {e}"