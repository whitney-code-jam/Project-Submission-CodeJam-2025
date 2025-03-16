"use client"
import React, { useState } from "react";
import { GoogleGenerativeAI } from "@google/generative-ai";

function MealPlanner() {
  const [foodChoice, setFoodChoice] = useState("");
  const [calories, setCalories] = useState("");
  const [mealList, setMealList] = useState([]);
  const [loading, setLoading] = useState(false);

  async function getMealSummary(food, calories) {
    setLoading(true);
    try {
      const genAI = new GoogleGenerativeAI("AIzaSyBUYEVnETYBxKXAOhWdoUh0IirNvKyDWMk");
      const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
      const prompt = `Provide a one-sentence short and concise summary of the nutritional value if any, of ${food} containing ${calories} calories. Also, classify it as healthy or unhealthy based on common dietary guidelines. If ${food} is not safe for human consumption, say It is not safe or ethical for human consumption. `;
      
      const result = await model.generateContent(prompt);
      const responseText = await result.response.text();
      return responseText;
    } catch (error) {
      console.error("Error fetching meal summary:", error);
      return "Could not generate summary.";
    } finally {
      setLoading(false);
    }
  }

  async function addMeal() {
    if (foodChoice && calories) {
      const summary = await getMealSummary(foodChoice, calories);

      const newMeal = {
        name: foodChoice,
        calories: calories,
        summary: summary,
      };

      setMealList([...mealList, newMeal]);
      setFoodChoice("");
      setCalories("");
    }
  }

  return (
    <div className="container">
      <h1 className="text-5xl">Meal Helper</h1>
      <input
        type="text"
        placeholder="What do you like to eat?"
        value={foodChoice}
        onChange={(e) => setFoodChoice(e.target.value)}
        className="input-box"
      />
      <input
        type="text"
        placeholder="Calories"
        value={calories}
        onChange={(e) => setCalories(e.target.value)}
        className="input-box"
      />
      <button onClick={addMeal} className="button" disabled={loading}>
        {loading ? "Loading..." : "Add Meal"}
      </button>
      <div className="meal-list">
        {mealList.map((meal, index) => (
          <div key={index} className="font-bold text-3xl">
            <h2>{meal.name}</h2>
            <p>{meal.calories} Calories</p>
            <p>Summary: {meal.summary}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MealPlanner;