from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cpp_output = ""
    if request.method == "POST":
        code = request.form["code"]

        # Save the input code
        with open("../py2cpp/demo.py", "w") as f:
            f.write(code)

        # Run transpiler and redirect output
        try:
            with open("../py2cpp/demo.cpp", "w") as outfile:
                result = subprocess.run(
                    ["python", "-m", "py2cpp", "../py2cpp/demo.py"],
                    stdout=outfile,
                    stderr=subprocess.PIPE,
                    text=True
                )
            if result.stderr:
                cpp_output = "[Error during transpilation]\n" + result.stderr
        except Exception as e:
            cpp_output = f"[Exception occurred: {e}]"

        # Read output
        if cpp_output == "":
            try:
                with open("../py2cpp/demo.cpp", "r") as f:
                    cpp_output = f.read()
            except FileNotFoundError:
                cpp_output = "[demo.cpp not found]"

    return render_template("index.html", output=cpp_output)

if __name__ == "__main__":
    app.run(debug=True)
