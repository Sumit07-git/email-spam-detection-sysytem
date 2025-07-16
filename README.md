# 📧 Email Spam Detection System

A machine learning-powered web application built with Streamlit that detects whether an email or message is spam or legitimate. The system uses Naive Bayes classification to analyze text content and provide real-time spam detection.

## 🚀 Features

- **Real-time Spam Detection**: Instantly classify messages as spam or safe
- **Interactive Web Interface**: User-friendly Streamlit interface with modern styling
- **Machine Learning Model**: Uses Multinomial Naive Bayes for accurate classification
- **Data Statistics**: View dataset statistics including total messages, spam count, and safe count
- **Example Messages**: Try predefined examples to test the system
- **Custom Styling**: Beautiful gradient headers and styled result boxes

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning library
- **CountVectorizer** - Text feature extraction
- **Multinomial Naive Bayes** - Classification algorithm

## 📁 Project Structure

```
spam/
│
├── app.py               # Main Streamlit application
├── spam.py              # SpamDetector class with ML model
├── ui.py                # UI components and styling
├── spam.csv             # Dataset file
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

```

## 🔧 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Sumit07-git/email-spam-detection-sysytem.git
cd spam-detection
```

2. **Install required packages**:
```bash
pip install streamlit pandas scikit-learn
```

3. **Prepare your dataset**:
   - Place your `spam.csv` file in the project directory
   - Ensure the CSV has columns: `Category` and `Message`
   - Category should contain `ham` (not spam) and `spam` values

## 📊 Dataset Format

Your `spam.csv` file should have the following structure:

```csv
Category,Message
ham,"Hi, how are you doing today?"
spam,"Congratulations! You've won $1000! Click here to claim now!"
ham,"Can we meet for lunch tomorrow?"
spam,"FREE! Click here for amazing deals!"
```

## 🚀 Usage

1. **Run the application**:
```bash
streamlit run app.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Use the application**:
   - Enter any message in the text area
   - Click "Analyze this message" to get results
   - Try example messages for quick testing
   - View dataset statistics in the metrics section

## 🔍 How It Works

1. **Data Loading**: The system loads and preprocesses the spam dataset
2. **Feature Extraction**: Uses CountVectorizer to convert text to numerical features
3. **Model Training**: Trains a Multinomial Naive Bayes classifier
4. **Prediction**: Analyzes new messages and classifies them as spam or safe
5. **Results Display**: Shows results with styled UI components

## 📈 Model Performance

The system uses:
- **CountVectorizer** with English stop words removal
- **Multinomial Naive Bayes** classifier
- **80/20 train-test split** for model validation

## 🎨 UI Features

- **Gradient Headers**: Modern styled headers with blue-green gradient
- **Result Boxes**: Color-coded results (red for spam, green for safe)
- **Example Section**: Pre-built examples for quick testing
- **Responsive Design**: Works well on different screen sizes
- **Interactive Elements**: Buttons and text areas with hover effects

## 📝 File Descriptions

### `app.py`
Main Streamlit application file that:
- Sets up the page configuration
- Loads the spam detector
- Displays the user interface
- Handles user interactions

### `spam.py`
Contains the `SpamDetector` class with methods:
- `load_and_train()`: Loads data and trains the model
- `predict()`: Predicts if a message is spam
- `get_stats()`: Returns dataset statistics

### `ui.py`
UI components and styling:
- `web_styles()`: CSS styling for the application
- `show_header()`: Displays the main header
- `show_result()`: Shows prediction results
- `show_examples()`: Displays example messages

## 🚨 Troubleshooting

**Common Issues:**

1. **File not found error**:
   - Ensure `spam.csv` exists in the correct path
   - Check file permissions

2. **Import errors**:
   - Install all required packages
   - Verify Python environment

3. **Model training fails**:
   - Check CSV file format
   - Ensure columns are named correctly

4. **Prediction errors**:
   - Make sure model is trained successfully
   - Check for empty input messages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by Sumit Samal

## 📞 Support

For issues or questions, please open an issue on the GitHub repository.
