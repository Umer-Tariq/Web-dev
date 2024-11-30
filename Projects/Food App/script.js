const searchBtn = document.querySelector('.header__btn');
const searchField = document.querySelector('.header__input');
const recipeContainer = document.querySelector('.recipe-container');
const containerHeader = document.querySelector('.header__main');

const searchRecipe = async (name) => {
    try {
        containerHeader.textContent = "Fetching Recipes...";
        const response = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${name}`);
        if (!response.ok) {
            containerHeader.textContent = "An error has occurred...";
        } else {
            const data = await response.json();
            if (data.meals) {
                containerHeader.textContent = ""; // Clear the header message
                recipeContainer.innerHTML = ""; // Clear previous recipes
                data.meals.forEach((meal) => {
                    // Create a recipe card
                    const recipeDiv = document.createElement('div');
                    recipeDiv.classList.add('recipe-item');
                    recipeDiv.innerHTML = `
                        <img src="${meal.strMealThumb}">
                        <h3>${meal.strMeal}</h3>
                        <p><span>${meal.strArea}</span> Dish</p>
                        <p>Belongs to <span>${meal.strCategory}</span> Category</p>
                    `;
                    recipeContainer.appendChild(recipeDiv);

                    // Add "View Recipe" button
                    const button = document.createElement('button');
                    button.classList.add('recipe-btn');
                    button.textContent = 'View Recipe';
                    recipeDiv.appendChild(button);

                    // Open popup on button click
                    button.addEventListener('click', () => {
                        openRecipePopUp(meal);
                    });
                });
            } else {
                containerHeader.textContent = "No Recipes found";
            }
        }
    } catch (error) {
        containerHeader.textContent = "An error has occurred...";
    }
};

const fetchIngredients = (meal) => {
    let ingredientsList = "";
    for (let i = 1; i <= 20; i++) {
        const ingredient = meal[`strIngredient${i}`];
        if (ingredient) {
            const measure = meal[`strMeasure${i}`];
            ingredientsList += `<li>${measure} ${ingredient}</li>`;
        } else {
            break;
        }
    }
    return ingredientsList;
};

const openRecipePopUp = (meal) => {
    // Remove any existing popup
    const existingRecipeDiv = document.querySelector('.recipe-div');
    if (existingRecipeDiv) {
        existingRecipeDiv.remove();
    }

    // Create a new popup
    const recipeDiv = document.createElement('div');
    recipeDiv.classList.add('recipe-div');
    recipeDiv.innerHTML = `
        <button type="button" class="close-btn btn"><i class="fa-regular fa-circle-xmark"></i></button>
        <div class="recipe-ingredients"></div>
        <div class="recipe-instructions"></div>
    `;
    recipeContainer.appendChild(recipeDiv);

    // Populate ingredients and instructions
    const recipeIngredient = recipeDiv.querySelector('.recipe-ingredients');
    recipeIngredient.innerHTML = `
        <h2>${meal.strMeal}</h2>
        <h3>Ingredients: </h3>
        <ul>${fetchIngredients(meal)}</ul>
    `;
    const recipeInstructions = recipeDiv.querySelector('.recipe-instructions');
    recipeInstructions.innerHTML = `
        <h3>Instructions: </h3>
        <p>${meal.strInstructions}</p>
    `;

    // Show popup with animation
    setTimeout(() => {
        recipeDiv.classList.add('show-popup');
    }, 10);

    // Add close button functionality
    const closeBtn = recipeDiv.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => {
        recipeDiv.remove(); // Remove popup from DOM
    });
};

// Attach search functionality
searchBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const recipeName = searchField.value.trim();
    searchRecipe(recipeName);
});
