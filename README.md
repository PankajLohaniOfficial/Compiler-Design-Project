# 🧬 Python to C++ Compiler

This is a **Python to C++ compiler** developed as part of a Compiler Design course. It includes a command-line compiler, a PyQt-based GUI for AST visualization, and a web interface for interactive use. The project is modular, extensible, and ideal for understanding compiler frontends and transpilation.

---

## 🚀 Features

- ✅ **Python to C++ Transpilation** – Converts Python scripts to C++ code.
- 🌳 **AST Viewer (GUI)** – Visualizes the abstract syntax tree using PyQt.
- 🌐 **Web Interface** – Flask app for easy web-based interactions.
- 🧪 **Unit Tests** – Built-in tests for core modules.
- 🔧 **Tooling Support** – Includes utility scripts for debugging and dumping AST.

---

## 📁 Project Structure

```
Compiler-Design-Project-main/
├── .gitattributes
├── LICENSE
├── README.md
├── helloworld.cpp
├── helloworld.py
├── main.py                    # Main compiler logic
├── requirements.txt          # Project dependencies
├── setup.py                  # Setup script
│
├── astviewer/                # PyQt GUI AST viewer
│   ├── main.py
│   ├── mainwindow.py
│   ├── models.py
│   ├── tools/
│   │   └── pyqt.sh
│   └── ui/
│       ├── .gitignore
│       ├── __init__.py
│       └── mainwindow.ui
│
├── include/py2cpp/           # C++ headers for translation
│   ├── py2cpp.hpp
│   └── range.hpp
│
├── py2cpp-web/               # Flask web interface
│   ├── app.py
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/script.js
│   └── templates/
│       └── index.html
│
├── py2cpp/                   # Python translation engine
│   ├── __init__.py
│   ├── __main__.py
│   ├── converter.py
│   ├── cpp.py
│   ├── docstring.py
│   ├── hook.py
│   ├── qt.py
│   ├── transformer.py
│   ├── types.py
│   ├── __pycache__/
│   └── tests/
│       ├── __init__.py
│       ├── test_converter.py
│       └── test_docstring.py
│
├── samples/                  # Sample Python and C++ programs
│   ├── add.cpp / add.py
│   ├── dp.cpp / dp.py
│   ├── helloworld.cpp / helloworld.py
│   └── range.cpp / range.py
│
├── tools/                    # Debug and dump tools
│   ├── cpp_dump.py
│   └── dump.py
│
└── venv/                     # (optional) Virtual environment
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd Compiler-Design-Project-main
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Use

### 👉 Run the Compiler

```bash
python main.py
```

### 👉 Launch the AST Viewer (GUI)

```bash
cd astviewer
python main.py
```

### 👉 Start the Web Interface

```bash
cd py2cpp-web
python app.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Run Tests

```bash
pytest py2cpp/tests/
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🙌 Contributions

Contributions are welcome! If you'd like to improve this project, feel free to fork, submit issues, or open pull requests.


# 📜 Contact

Fell free for contacting in the gmail - [Email](pankajlohani2023@gmail.com)
