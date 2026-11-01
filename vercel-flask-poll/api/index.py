from flask import Flask, render_template_string, request

app = Flask(__name__)

# Anonymous in-memory tallies (reset when the server restarts)
votes = {"yes": 0, "no": 0}

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Demo Poll</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      background: #f4f4f8;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: white;
      padding: 40px 50px;
      border-radius: 16px;
      box-shadow: 0 6px 24px rgba(0,0,0,.1);
      text-align: center;
    }
    h1 { margin-top: 0; }
    button {
      font-size: 1.1rem;
      padding: 12px 36px;
      margin: 8px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      color: white;
    }
    .yes { background: #4caf50; }
    .no  { background: #e53935; }
    button:hover { opacity: .85; }
  </style>
</head>
<body>
  <div class="card">
    {% if answered %}
      <h1>Thanks for answering!</h1>
      <p>You answered: <strong>{{ answer }}</strong></p>
      <p>Yes: {{ votes.yes }} &nbsp;|&nbsp; No: {{ votes.no }}</p>
      <a href="/">Back</a>
    {% else %}
      <h1>Are you gay?</h1>
      <form method="post">
        <button class="yes" name="answer" value="yes">Yes</button>
        <button class="no" id="no" name="answer" value="no">No</button>
      </form>
    {% endif %}
  </div>

  <script>
    const noBtn = document.getElementById("no");
    if (noBtn) {
      const dodge = () => {
        noBtn.style.position = "fixed";
        const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
        const y = Math.random() * (window.innerHeight - noBtn.offsetHeight);
        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";
      };
      noBtn.addEventListener("mouseover", dodge);
      noBtn.addEventListener("touchstart", (e) => { e.preventDefault(); dodge(); });
    }
  </script>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer in votes:
            votes[answer] += 1
            return render_template_string(
                PAGE, answered=True, answer=answer.capitalize(), votes=votes
            )
    return render_template_string(PAGE, answered=False)


if __name__ == "__main__":
    app.run(debug=True)
