import { useState } from "react";
import "./App.css";

function App() {

  const [review, setReview] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeReview = async () => {

    if (!review.trim()) {
      alert("Please enter a review");
      return;
    }

    setLoading(true);

    try {

      const response = await fetch(
        "http://127.0.0.1:5000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            review: review
          })
        }
      );

      const data = await response.json();

      setResult(data.prediction);

    } catch (error) {

      setResult("Server Error");

    }

    setLoading(false);
  };

  return (

    <div className="app">

      {/* Background Blur */}
      <div className="bg1"></div>
      <div className="bg2"></div>

      {/* Navbar */}
      <nav className="navbar">

        <h2>
          AI Review Analyzer
        </h2>

      </nav>

      {/* Main Card */}
      <div className="main-container">

        <div className="glass-card">

          <h1 className="title">
            AI Fake Review Detector
          </h1>

          <p className="subtitle">
            Analyze reviews instantly using
            Artificial Intelligence & Machine Learning
          </p>

          {/* Textarea */}
          <textarea
            placeholder="Write or paste a review here..."
            value={review}
            onChange={(e) => setReview(e.target.value)}
          />

          {/* Buttons */}
          <div className="button-group">

            <button
              className="analyze-btn"
              onClick={analyzeReview}
            >

              {loading ? "Analyzing..." : "Analyze Review"}

            </button>

            <button
              className="clear-btn"
              onClick={() => {
                setReview("");
                setResult("");
              }}
            >
              Clear
            </button>

          </div>

          {/* Result */}
          {result && (

            <div className={`result-box 
              ${result.includes("Fake")
                ? "fake"
                : "real"
              }`}>

              {result}

            </div>
          )}

        </div>

      </div>

    </div>
  );
}

export default App;