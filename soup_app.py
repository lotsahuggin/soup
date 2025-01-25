import streamlit as st
import random

# Set up dictionaries for flavour profiles and dietary restrictions

ingredient_properties = {
    "butternut squash": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "sweet potato": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "carrot": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "tomato": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "mushroom": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "lentil": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "chickpea": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "black bean": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "broccoli": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "cauliflower": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "potato": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "onion": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "leek": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "celery": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "spinach": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "kale": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "corn": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "pea": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "asparagus": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "green bean": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "courgette": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "bell pepper": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "red lentil": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "yellow split pea": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "cannellini bean": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "butter bean": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "parsnip": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "turnip": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "rutabaga": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "watercress": {"vegan": True, "vegetarian": True, "gluten-free": True},
    "ham": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "bread": {"vegan": True, "vegetarian": True, "gluten-free": False},
    "chicken": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "beef": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "lamb": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "pork": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "salmon": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "tuna": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "mackerel": {"vegan": False, "vegetarian": False, "gluten-free": True},
    "egg": {"vegan": False, "vegetarian": True, "gluten-free": True},
    "milk": {"vegan": False, "vegetarian": True, "gluten-free": True},
    "cheese": {"vegan": False, "vegetarian": True, "gluten-free": True},
    "yogurt": {"vegan": False, "vegetarian": True, "gluten-free": True},
    "butter": {"vegan": False, "vegetarian": True, "gluten-free": True},
    "cream": {"vegan": False, "vegetarian": True, "gluten-free": True},
    # ... add more ingredients and their properties
}

flavour_profiles = {
    "sweet": ["butternut squash", "sweet potato", "carrot", "corn"],
    "savoury": ["mushroom", "lentil", "chickpea", "black bean", "onion", "celery"],
    "spicy": ["chilli flakes", "hot sauce", "jalapeno"],
    "earthy": ["potato", "leek", "kale", "spinach", "mushroom"]
    # ... add more flavour profiles
}

# Initialize session state for previous recipes
if "previous_recipes" not in st.session_state:
    st.session_state.previous_recipes = []

def generate_recipe(flavour_profile, dietary_restrictions):
    adjectives = [
        "Creamy", "Hearty", "Spicy", "Tangy", "Zesty", "Savoury", "Sweet", "Smoky",
        "Garlicky", "Lemony", "Rich", "Velvety", "Smooth", "Chunky", "Rustic",
        "Delicate", "Flavourful", "Aromatic", "Comforting", "Warm", "Refreshing",
        "Light", "Vibrant", "Earthy", "Nutty", "Herby", "Tangy", "Fruity", "Fiery",
        "Mild", "Savoury"
    ]
    main_ingredients = [
        "butternut squash", "sweet potato", "carrot", "tomato", "mushroom",
        "lentil", "chickpea", "black bean", "broccoli", "cauliflower", "potato",
        "onion", "leek", "celery", "spinach", "kale", "corn", "pea", "asparagus",
        "green bean", "courgette", "bell pepper", "red lentil", "yellow split pea",
        "cannellini bean", "butter bean", "parsnip", "turnip", "rutabaga", "watercress",
        "ham", "chicken", "beef", "lamb", "pork", "salmon", "tuna", "mackerel"
    ]
    cooking_methods = [
        "roasted", "sautéed", "grilled", "fried", "baked", "steamed", "simmered",
        "braised", "poached", "blanched", "puréed", "stir-fried", "pan-fried",
        "deep-fried", "air-fried", "broiled", "charred", "smoked", "pickled",
        "fermented", "caramelised", "confit", "flambéed", "sous vide", "pressure-cooked",
        "slow-cooked", "stewed", "infused", "reduced", "glazed"
    ]
    garnish_ingredients = [
        "peppers", "crispy onions", "croutons", "pine nuts", "sesame seeds",
        "pumpkin seeds", "fresh herbs", "chilli flakes", "lemon zest", "lime zest",
        "grated cheese", "toasted almonds", "chopped walnuts", "sunflower seeds",
        "hemp seeds", "flax seeds", "chia seeds", "pomegranate seeds", "cranberries",
        "raisins", "chopped dates", "coconut flakes", "chocolate shavings", "caramel sauce",
        "balsamic glaze", "sriracha sauce", "hot sauce", "salsa", "guacamole", "pesto", "lardons"
    ]
    
    side_dishes = [
        "crusty bread", "garlic bread", "grilled cheese sandwich", "salad", "rice",
        "quinoa", "couscous", "pasta", "noodles", "potatoes", "sweet potato fries",
        "roasted vegetables", "coleslaw", "cornbread", "biscuits", "crackers",
        "pita bread", "naan bread", "tortilla chips", "flatbread", "dumplings",
        "spring rolls", "samosas", "falafel", "hummus", "tzatziki", "olives",
        "pickles", "chutney", "kimchi"
    ]

    # Pick a random adjective at the start
    adjective = random.choice(adjectives)

    # Filter ingredients for the user's flavour profiles and dietary restrictions
    filtered_ingredients = main_ingredients.copy()  # Start with all ingredients

    if flavour_profile != "Any":
        filtered_ingredients = [
            ingredient for ingredient in filtered_ingredients
            if ingredient in flavour_profiles[flavour_profile]
        ]

    for restriction in dietary_restrictions:
        filtered_ingredients = [
            ingredient for ingredient in filtered_ingredients
            if ingredient_properties[ingredient][restriction.lower()]
        ]

    main_ingredient1 = random.choice(filtered_ingredients)
    main_ingredient2 = random.choice(filtered_ingredients)

    # Ensure main ingredients are different
    while main_ingredient1 == main_ingredient2:
        main_ingredient2 = random.choice(main_ingredients)

    cooking_method = random.choice(cooking_methods)
    garnish_ingredient = random.choice(garnish_ingredients)
    side_dish = random.choice(side_dishes)

    recipe = f"{adjective} {main_ingredient1} and {main_ingredient2} soup, garnished with {cooking_method} {garnish_ingredient}, served with a side of {side_dish}."
    return recipe


st.title("Random Soup Recipe Generator")

# Let user set conditions for their recipe

flavour_profile = st.selectbox("Select a flavour profile:", ["Any"] + list(flavour_profiles.keys()))

dietary_restrictions = st.multiselect(
    "Select dietary restrictions:",
    ["Vegan", "Vegetarian", "Gluten-free"]
)

if st.button("Generate Recipe"):
    recipe = generate_recipe(flavour_profile, dietary_restrictions)
    st.write(recipe)

    # Update previous recipes
    st.session_state.previous_recipes.insert(0, recipe)
    st.session_state.previous_recipes = st.session_state.previous_recipes[:4]

# Display previous recipes with varying shades of grey
grey_shades = ["#A9A9A9", "#B0B0B0", "#D3D3D3", "#F0F0F0"]
for i, prev_recipe in enumerate(st.session_state.previous_recipes):
    st.markdown(f"<p style='color:{grey_shades[i]};padding:5px;'>{prev_recipe}</p>", unsafe_allow_html=True)