document.getElementById('exerciseForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const age = parseInt(document.getElementById('age').value);
  const weight = parseInt(document.getElementById('weight').value);
  const height = parseInt(document.getElementById('height').value);
  const fitnessLevel = document.getElementById('fitnessLevel').value;
  const goal = document.getElementById('goal').value;

  const recommendedExercises = getExercises(age, weight, height, fitnessLevel, goal);
  displayRecommendations(recommendedExercises, goal);
});

function getExercises(age, weight, height, fitnessLevel, goal) {
  let exercises = [];

  // General Exercises Based on Fitness Level
  if (fitnessLevel === 'beginner') {
    exercises.push('Walking (30 minutes)');
    exercises.push('Bodyweight Squats (3 sets of 10)');
    exercises.push('Plank (30 seconds)');
  } else if (fitnessLevel === 'intermediate') {
    exercises.push('Jogging (30 minutes)');
    exercises.push('Push-ups (3 sets of 15)');
    exercises.push('Lunges (3 sets of 12 each leg)');
    exercises.push('Plank (1 minute)');
  } else if (fitnessLevel === 'advanced') {
    exercises.push('Running (45 minutes)');
    exercises.push('Pull-ups (3 sets of 10)');
    exercises.push('Burpees (3 sets of 15)');
    exercises.push('Plank (2 minutes)');
  }

  // Goal-Specific Adjustments
  if (goal === 'weightLoss') {
    exercises.push('High-intensity interval training (HIIT)');
    exercises.push('Jump rope (10 minutes)');
    exercises.push('Mountain climbers (3 sets of 20)');
  } else if (goal === 'strength') {
    exercises.push('Deadlifts (3 sets of 8)');
    exercises.push('Bench press (3 sets of 8)');
    exercises.push('Pull-ups (3 sets of 10)');
  } else if (goal === 'cardio') {
    exercises.push('Running (45 minutes)');
    exercises.push('Cycling (30 minutes)');
    exercises.push('Swimming (30 minutes)');
  }

  // Age-Specific Adjustments
  if (age > 35) {
    exercises.push('Gentle Yoga');
    exercises.push('Swimming');
  }

  // Weight-Specific Adjustments
  if (weight > 150) {
    exercises.push('Walking (low-impact)');
    exercises.push('Cycling (easy pace)');
    exercises.push('Water Aerobics');
  }

  return exercises;
}

function displayRecommendations(exercises, goal) {
  const exerciseList = document.getElementById('exerciseList');
  exerciseList.innerHTML = '';
  
  exercises.forEach(exercise => {
    const exerciseItem = document.createElement('p');
    exerciseItem.textContent = exercise;
    exerciseList.appendChild(exerciseItem);
  });

  const goalMessage = document.getElementById('goalMessage');
  goalMessage.innerHTML = `<p>Your fitness goal is: <strong>${goal}</strong></p>`;
  
  document.getElementById('exercise-recommendations').style.display = 'block';
}
