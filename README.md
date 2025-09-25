💰 Personal Finance & Expense Analyzer




A data analysis tool to track and analyze personal expenses.
This project helps users understand income vs. expenses, detect unusual transactions, and visualize financial trends.

🚀 Features

📂 Data Cleaning & Processing with Pandas

📊 Monthly summaries & savings ratios

⚠️ Anomaly Detection (spot unusual spending or income)

📈 Interactive Visualizations:

Income vs. Expenses

Category-wise Spending

Trend Analysis over Time

🛠️ Tech Stack

Python 3.10+

Pandas (data manipulation)

NumPy (statistical analysis)

Matplotlib (visualizations)

📂 Project Structure
Expense-Analyzer/
│── data/
│   └── expenses_500.csv          # Sample dataset
│── src/
│   ├── data_loader.py            # Load and preprocess dataset
│   ├── analyzer.py               # Summaries & anomaly detection
│   ├── visualizer.py             # Plotting functions
│   └── main.py                   # Main entry point
│── requirements.txt
│── README.md
└── .gitignore

⚡ Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/rahulpajjuri12/Personal-Finance-and-Expenses-Analyzer.git
cd Personal-Finance-and-Expenses-Analyzer

2️⃣ Create Virtual Environment
python -m venv myenv


Activate it:

Windows: myenv\Scripts\activate

Mac/Linux: source myenv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Project
python src/main.py

📊 Example Visualizations

📌 Sample plots will be generated from expenses_500.csv

Income vs Expenses

Spending by Category

Monthly Trends

Add screenshots here once you run the project.

📌 Future Improvements

Web dashboard (Flask/Django/Streamlit)

Export reports to PDF/Excel

Predictive insights with ML

📜 License

This project is licensed under the MIT License.
