# StockPulse 📈

StockPulse is a comprehensive stock market analysis and prediction application built with Streamlit. It empowers users to track real-time stock data, visualize complex financial indicators, and leverage both statistical and deep learning models to forecast future stock trends.

## 🚀 Features

*   **Real-time Stock Analysis:** specific details, company information, and historical data visualization using `yfinance`.
*   **Interactive Visualizations:**
    *   **Stock Display:** View raw data and Bollinger Bands overlaid on stock prices.
    *   **Interactive Charts:** Dynamic plots using Plotly and Matplotlib for deep insights.
*   **Advanced Predictions:**
    *   **Prophet Forecasting (Predict I):** Utilizes Facebook's Prophet model to forecast stock prices up to 4 years into the future, complete with trend components.
    *   **Deep Learning Prediction:** Uses a pre-trained Keras/TensorFlow model (LSTM-based) to predict stock trends, comparing 100-day and 200-day moving averages against actual closing prices.
*   **User Management:** Secure Sign-up and Login functionality powered by **Google Firebase Authentication**.
*   **Personalized Watchlist:** Save and manage your favorite stocks in a personalized watchlist, synced across devices using **Firebase Firestore**.

## 🛠️ Tech Stack

*   **Frontend/Framework:** [Streamlit](https://streamlit.io/)
*   **Data Analysis:** Pandas, NumPy, yfinance, Pandas Datareader
*   **Machine Learning & AI:**
    *   [TensorFlow/Keras](https://www.tensorflow.org/) (Deep Learning)
    *   [Prophet](https://facebook.github.io/prophet/) (Time-series forecasting)
    *   Scikit-learn
*   **Visualization:** Matplotlib, Plotly, Cufflinks
*   **Backend/Database:** Google Firebase (Auth & Firestore)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
*   [Python 3.9+](https://www.python.org/downloads/)
*   A Google Firebase project with Authentication (Email/Password) and Firestore Database enabled.

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd StockPulse
    ```

2.  **Install Dependencies**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If you are on Apple Silicon (M1/M2/M3), you might need to install `tensorflow-macos` specifically if standard installation fails.*

3.  **Firebase Configuration**
    *   Go to your [Firebase Console](https://console.firebase.google.com/).
    *   Settings > Project Settings > Service Accounts.
    *   Click **Generate new private key**.
    *   Rename the downloaded JSON file to `stockpulse-b1818-afca9e4f09d8.json` (or update the filename in `Watchlist.py`) and place it in the root directory.
    *   **Important:** You also need a generic `Insert Google-api-key.json` or update `Account.py` line 8 to point to your valid service account key file.

4.  **Path Configuration (Critical Fix Required)**
    Open `DeepPrediction.py` and locate the line loading the model (around line 63):
    ```python
    model = load_model(r'C:\Users\vaibhav_gudali\Desktop\MAIN PROJECT\Stockpulse\keras_model.h5')
    ```
    **Change this to a relative path:**
    ```python
    model = load_model('keras_model.h5')
    ```

6.  **Security & Configuration**
    To run the application, you must provide Firebase credentials via an environment variable to ensure security.
    *   **Get your credentials**: Open your `stockpulse-b1818-afca9e4f09d8.json` (or whichever service account file you downloaded).
    *   **Minify the JSON**: Convert the multi-line JSON into a single line string. You can use a tool like `jq -c . stockpulse-b1818-afca9e4f09d8.json` or an online minifier.
    *   **Set the environment variable**:
        ```bash
        export FIREBASE_CREDENTIALS='{"type": "service_account", "project_id": "..."}'
        ```
    *   **Run the app**:
        ```bash
        streamlit run main.py
        ```
    *   **Note**: Ensure `*.json` files containing secrets are NOT committed to Git.

## ▶️ Usage

Run the main application using Streamlit:

```bash
streamlit run main.py
```

Navigate to the URL provided in the terminal (usually `http://localhost:8501`) to access the app.

## 📂 Project Structure

*   `main.py`: The entry point of the application, handling navigation between different modules.
*   `Home.py`: The landing page with a general overview.
*   `Account.py`: Handles user login and signup using Firebase Auth.
*   `Display.py`: detailed stock metrics and Bollinger Bands.
*   `Predict.py`: Stock forecasting using the Prophet model.
*   `DeepPrediction.py`: Deep learning-based predictions using the `keras_model.h5`.
*   `Watchlist.py`: Manages the user's favorite stocks using Firebase Firestore.
*   `keras_model.h5`: The pre-trained deep learning model file.
