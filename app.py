from flask import Flask, render_template, request
from parser import extract_resume_text
from ranking import get_ats_score

app = Flask(__name__)

# Initialize results as a global variable
all_results = []

@app.route("/")
def home():
    return render_template("page.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/rest")
def rest():
    # Safely pass results (can be empty)
    return render_template("rest.html", title="Result", results=all_results)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/ats", methods=["GET", "POST"])
def ats_page():
    global all_results
    all_results = []

    if request.method == "POST":
        uploaded_files = request.files.getlist("resume")
        jd = request.form.get("jd")

        if not uploaded_files or not jd:
            return render_template("ats.html", results=[], error="Please upload a resume and enter JD")

        for file in uploaded_files:
            filename = file.filename
            content = file.read()

            text, skills, exp = extract_resume_text(filename, content)
            score, matched, missing = get_ats_score(text, jd)

            all_results.append({
                "name": filename,
                "score": float(score),
                "matched": matched,
                "missing": missing
            })

        print("All Results:", all_results)

        # Go to separate page for graph
        return render_template("rest.html", results=all_results)

    return render_template("ats.html")

if __name__ == "__main__":
    app.run(debug=True, port=5085)
