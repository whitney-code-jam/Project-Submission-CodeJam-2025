// server.mjs
import express from "express";
import fetch from "node-fetch";
import cors from "cors";

const app = express();
const PORT = process.env.PORT || 5000;

// Enable CORS to allow requests from your React app
app.use(cors());

// Middleware to parse JSON bodies
app.use(express.json());

// Replace with your Gemini API Key
const GEMINI_API_KEY = "AIzaSyCH4Rui-bxEU5AJpu3hqaf3LWiGsl_iUVY";

// Endpoint to handle meal summary request
app.post("/api/getMealSummary", async (req, res) => {
  const { food, calories } = req.body;

  if (!food || !calories) {
    return res.status(400).json({ error: "Food and calories are required." });
  }

  try {
    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GEMINI_API_KEY}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          contents: [
            {
              parts: [
                {
                  text: `Analyze the meal: ${food} with ${calories} calories. Provide a short health-related summary.`,
                },
              ],
            },
          ],
        }),
      }
    );

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    const data = await response.json();
    const summary =
      data?.candidates?.[0]?.content?.parts?.[0]?.text || "No summary available.";

    return res.json({ summary });
  } catch (error) {
    console.error("Error:", error);
    return res.status(500).json({ error: "Error fetching summary." });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
