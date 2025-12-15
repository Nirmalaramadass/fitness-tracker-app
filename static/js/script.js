document.addEventListener("DOMContentLoaded", function () {
    fetchFitnessData();
});

function fetchFitnessData() {
    const loaderEl = document.getElementById("loader");
    if (loaderEl) loaderEl.style.display = "block";

    fetch("/api/fitness")
        .then(response => response.json())
        .then(data => {
            // Totals (if elements exist)
            const totalStepsEl = document.getElementById("totalSteps");
            const totalCaloriesEl = document.getElementById("totalCalories");
            const weightEl = document.getElementById("weight");
            const heightEl = document.getElementById("height");

            if (totalStepsEl) totalStepsEl.textContent = data.total_steps ?? "N/A";
            if (totalCaloriesEl) totalCaloriesEl.textContent = data.total_calories_burned ?? "N/A";
            if (weightEl) weightEl.textContent = data.weight ? data.weight + " kg" : "N/A";
            if (heightEl) heightEl.textContent = data.height ? data.height + " cm" : "N/A";

            // Prepare labels Mon-Sun
            const labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
            // Use provided daily arrays or empty arrays
            const dailySteps = Array.isArray(data.daily_steps) ? data.daily_steps.slice(0,7) : [];
            const dailyCalories = Array.isArray(data.daily_calories_burned) ? data.daily_calories_burned.slice(0,7) : [];

            // Ensure arrays length match labels (pad with zeros if shorter)
            while (dailySteps.length < 7) dailySteps.push(0);
            while (dailyCalories.length < 7) dailyCalories.push(0);

            // Steps Chart
            const stepsEl = document.getElementById('stepsChart');
            if (stepsEl) {
                const ctx = stepsEl.getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Steps',
                            data: dailySteps,
                            borderColor: '#6be0ff',
                            backgroundColor: 'rgba(107,224,255,0.12)',
                            fill: true,
                            tension: 0.4,
                            pointRadius: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        interaction: { mode: 'index', intersect: false },
                        plugins: {
                            tooltip: {
                                enabled: true,
                                callbacks: {
                                    label: function(context) { return context.dataset.label + ': ' + context.formattedValue; }
                                }
                            },
                            legend: { display: false }
                        },
                        scales: {
                            x: { title: { display: true, text: 'Day' } },
                            y: { beginAtZero: true, title: { display: true, text: 'Steps Count' } }
                        },
                        animation: { duration: 800, easing: 'easeOutQuart' }
                    }
                });
            }

            // Calories Chart
            const calEl = document.getElementById('caloriesChart');
            if (calEl) {
                const ctx2 = calEl.getContext('2d');
                new Chart(ctx2, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Calories burned',
                            data: dailyCalories,
                            backgroundColor: 'rgba(255,94,98,0.85)'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        interaction: { mode: 'index', intersect: false },
                        plugins: {
                            tooltip: {
                                enabled: true,
                                callbacks: {
                                    label: function(context) { return context.dataset.label + ': ' + context.formattedValue + ' kcal'; }
                                }
                            },
                            legend: { display: false }
                        },
                        scales: {
                            x: { title: { display: true, text: 'Day' } },
                            y: { beginAtZero: true, title: { display: true, text: 'Calories (kcal)' } }
                        },
                        animation: { duration: 800, easing: 'easeOutQuart' }
                    }
                });
            }

        })
        .catch(error => {
            console.error("Error fetching fitness data:", error);
        })
        .finally(() => { if (loaderEl) loaderEl.style.display = "none"; });
}
