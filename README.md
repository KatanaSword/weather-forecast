# Weather Forecast App

A command-line interface (CLI) application that provides real-time weather forecasts for a specified city using the Tomorrow.io API.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/KatanaSword/weather-forecast-cli.git
   cd weather-forecast-cli
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv .venv
   .\.venv\Scripts\activate  # On Mac use `source .venv/bin/activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the project root directory and add your [Tomorrow](https://app.tomorrow.io/) API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

Run the Weather Forecast App:

```sh
python app.py
```

Follow the on-screen menu to get the weather forecast for a city:

1. Get weather forecast
2. Exit app

## Environment Variables

API_KEY: Your [Tomorrow](https://app.tomorrow.io/) API key for accessing the weather data.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
