# RTCFR Meal Planner Prompt

## Project Overview

This project defines a professional prompt for creating a **7-day South Indian vegetarian meal plan** designed for a working professional in Tamil Nadu who spends most of the day at a desk.

The primary objective is **healthy, sustainable weight loss** while keeping meals practical, affordable, easy to prepare, and suitable for carrying to the office.

The prompt also requires an **image-generation prompt for every meal**, allowing each dish to be rendered as premium, appetizing food photography using **DALL·E 3**.

---

## RTCFR Prompt Structure

### Role

Act as a highly professional, Certified Nutritionist specializing in South Indian cuisine.

### Task

Create a comprehensive 7-day meal plan.

For every meal provided:

1. Give a practical meal recommendation.
2. Specify clear portion sizes.
3. Include approximate calories.
4. Create a detailed, highly attractive **Image Prompt** for the meal.
5. Make the image prompt suitable for generating a premium food image with **DALL·E 3**.

The meal plan should support healthy weight loss without being unnecessarily restrictive.

---

## Context

The client is:

- A working professional based in **Tamil Nadu**
- Mostly sedentary because of an office-based desk job
- Following a **strictly vegetarian** diet
- Primarily interested in **healthy weight loss**
- Looking for simple, locally available ingredients
- Interested in traditional and familiar **South Indian/Tamil Nadu cuisine**
- In need of meals that are practical for office preparation and packing

### Dietary Requirements

The recommendations should:

- Remain strictly vegetarian.
- Prioritize vegetables, whole grains, millets, pulses, legumes, and fiber-rich foods.
- Use traditional Tamil Nadu and South Indian ingredients where practical.
- Keep coconut and high-calorie ingredients moderate.
- Avoid unnecessary deep-fried foods.
- Provide sensible portion sizes.
- Include balanced combinations of carbohydrates, protein, vegetables, and healthy fats.
- Prefer meals that can be prepared with simple household ingredients.
- Include office-friendly meals that can be packed easily.
- Avoid overly complicated recipes.

> **Note:** Calorie values are approximate and should be treated as practical estimates rather than medical prescriptions.

---

## Few-Shot Examples

### Example 1 — Breakfast

**Breakfast Recommendation:**  
2 Ragi (finger millet) idlis with a side of mixed vegetable sambar, using minimal coconut to reduce calories.

**Image Prompt:**  
*Professional food photography of two steaming ragi idlis served on a fresh green banana leaf, accompanied by a vibrant colorful bowl of mixed vegetable sambar, warm morning sunlight, highly detailed, appetizing South Indian breakfast presentation, photorealistic, premium commercial food styling, 8k-quality detail.*

---

### Example 2 — Lunch

**Lunch Recommendation:**  
1 cup of Kodo millet lemon rice with a side of cucumber and carrot kosambari and a small portion of plain yogurt.

**Image Prompt:**  
*A beautifully arranged sleek glass bento box on a wooden office desk, featuring bright yellow Kodo millet lemon rice garnished with curry leaves, alongside fresh crisp cucumber and carrot kosambari and a small portion of plain yogurt, bright natural lighting, appetizing commercial food styling, clean office-lunch presentation, photorealistic.*

---

## Required Response Format

The final response must be presented as a clean, professional **day-wise table** covering all 7 days.

Use approximately the following structure:

| Day | Breakfast | Lunch | Dinner | Approximate Calories |
|---|---|---|---|---|
| Monday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Tuesday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Wednesday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Thursday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Friday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Saturday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |
| Sunday | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | Meal recommendation + *[Image Prompt]* | ~XXX kcal |

### Formatting Rules

Inside each meal cell:

- Show the **meal recommendation first**.
- Show the corresponding **Image Prompt** immediately below it.
- Format the Image Prompt in *italics*.
- Clearly state portion sizes.
- Keep the language professional and easy to understand.

---

## Meal Planning Guidelines

### Breakfast

Breakfast should generally:

- Provide adequate fiber and sustained energy.
- Use options such as idli, dosa, ragi, oats, millets, upma, adai, vegetable preparations, and similar South Indian foods.
- Avoid excessive oil.
- Include protein-rich accompaniments where possible.

Examples:

- Ragi idli + vegetable sambar
- Vegetable dosa + sambar
- Ragi adai + vegetable chutney
- Oats with fruit and nuts
- Vegetable upma
- Sprouted moong salad + whole-grain toast

### Lunch

Lunch should generally:

- Be easy to carry to an office.
- Use leak-proof containers or bento-box-friendly meals.
- Combine whole grains/millets with vegetables and protein-rich sides.
- Include curd, buttermilk, salad, dal, legumes, or similar accompaniments where appropriate.

Examples:

- Kodo millet lemon rice + kosambari + curd
- Vegetable quinoa salad + moong dal
- Vegetable pulao + raita + salad
- Lemon rice + chana salad + curd
- Vegetable sambar rice + cucumber salad + buttermilk

### Dinner

Dinner should generally:

- Be lighter than lunch.
- Emphasize vegetables and moderate portions of grains.
- Avoid heavy, oily, or deep-fried foods.
- Be practical for a working professional returning home after office hours.

Examples:

- Vegetable soup + steamed sweet corn
- Kootu + phulka + salad
- Mixed vegetable soup + light grain accompaniment
- Stuffed capsicum + millet roti + salad
- Tomato rasam + steamed vegetables + small rice portion

---

## Image Prompt Standards

Every meal must have its own image-generation prompt.

The image prompt should describe:

- The exact dish
- Portion and serving presentation
- Supporting side dishes
- Plate, banana leaf, bowl, tiffin box, or bento-box presentation as appropriate
- South Indian visual identity
- Fresh ingredients and appetizing textures
- Natural or premium studio lighting
- Professional food styling
- Photorealistic appearance
- High-detail commercial food photography

### DALL·E 3 Image Generation

Use **DALL·E 3** to render the meal images based on the generated Image Prompts.

Recommended visual characteristics:

- Photorealistic
- Premium food photography
- Natural food textures
- Appetizing presentation
- Clean composition
- High detail
- Warm, realistic lighting
- Contemporary commercial styling
- South Indian/Tamil Nadu cultural authenticity

Avoid:

- Artificial-looking food
- Excessive garnish
- Unrealistic portions
- Plastic-looking textures
- Overly saturated colors
- Non-vegetarian ingredients
- Unrelated Western dishes
- Ambiguous or unidentifiable food

---

## Example Weekly Meal Plan Categories

A balanced weekly plan can rotate among:

- Idli and millet idli
- Dosa
- Ragi adai
- Vegetable upma
- Oats
- Sprouts
- Millet rice
- Vegetable pulao
- Lemon rice
- Sambar rice
- Kootu
- Phulka
- Rasam
- Vegetable soups
- Kosambari and fresh salads
- Curd and buttermilk
- Seasonal fruits
- Small portions of nuts and seeds

The plan should provide sufficient variety across the seven days so that meals do not feel repetitive.

---

## Calorie Presentation

Show approximate daily calories in the final column.

Example:

- Monday — ~1,350 kcal
- Tuesday — ~1,400 kcal
- Wednesday — ~1,300 kcal

Calorie values should remain realistic and internally consistent with the stated portions.

Do not present calorie estimates as exact medical prescriptions.

---

## Professional Quality Checklist

Before producing the final answer, verify that:

- [ ] All 7 days are included.
- [ ] Breakfast, lunch, and dinner are included for every day.
- [ ] Every meal has a clear portion size.
- [ ] Every meal contains a corresponding Image Prompt.
- [ ] Image Prompts are formatted in italics.
- [ ] Meals are strictly vegetarian.
- [ ] Ingredients are practical for Tamil Nadu.
- [ ] Office-friendly lunch options are included.
- [ ] Calorie estimates are provided.
- [ ] Food choices support healthy weight loss.
- [ ] The table is clean and easy to read.
- [ ] Image prompts are detailed enough for DALL·E 3.
- [ ] The overall presentation looks professional and visually engaging.

---

## Master Prompt

Use the following prompt directly with an AI system:

> **Role:** Act as a highly professional, Certified Nutritionist specializing in South Indian cuisine.
>
> **Task:** Create a comprehensive 7-day meal plan for healthy weight loss. For every meal provided, give a clear portion size, an approximate calorie estimate, and a detailed, highly attractive Image Prompt suitable for DALL·E 3.
>
> **Context:** The client is a working professional based in Tamil Nadu who spends most of the day at an office desk. The diet must be strictly vegetarian. The primary goal is healthy, sustainable weight loss. Use simple, locally available South Indian ingredients and include practical office-friendly meals that are easy to pack and carry.
>
> Prioritize vegetables, millets, whole grains, pulses, legumes, fiber-rich foods, and moderate amounts of healthy fats. Minimize unnecessary oil, coconut, deep-fried foods, and highly processed ingredients. Keep portions realistic and balanced.
>
> **Few Shots:**
>
> **Breakfast Recommendation:** 2 Ragi (finger millet) idlis with a side of mixed vegetable sambar, minimizing coconut to reduce calories.
>
> **Image Prompt:** *Professional food photography of two steaming ragi idlis served on a fresh green banana leaf, accompanied by a vibrant colorful bowl of mixed vegetable sambar, warm morning sunlight, highly detailed, appetizing South Indian breakfast presentation, photorealistic, premium commercial food styling.*
>
> **Lunch Recommendation:** 1 cup of Kodo millet lemon rice with a side of cucumber and carrot kosambari and a small portion of plain yogurt.
>
> **Image Prompt:** *A beautifully arranged sleek glass bento box on a wooden office desk, featuring bright yellow Kodo millet lemon rice garnished with curry leaves, alongside fresh crisp cucumber and carrot kosambari and a small portion of plain yogurt, bright natural lighting, appetizing commercial food styling, clean office-lunch presentation, photorealistic.*
>
> **Response Format:** Deliver the output as a clean, professional day-wise table covering all 7 days.
>
> Use the columns:
>
> **Day | Breakfast | Lunch | Dinner | Approximate Calories**
>
> Inside every breakfast, lunch, and dinner cell, include:
>
> 1. Meal recommendation
> 2. Portion size
> 3. *[Image Prompt]* in italics
>
> Ensure each Image Prompt is visually detailed and suitable for DALL·E 3 image generation.
>
> Make the final result professional, attractive, practical, calorie-conscious, and suitable for a Tamil Nadu office professional following a vegetarian weight-loss diet.

---

## Intended Outcome

The completed output should function as both:

1. A practical 7-day vegetarian meal-planning guide.
2. A visual content-generation guide where each meal can be rendered as a premium food image using DALL·E 3.

The result should be easy to read, visually engaging, and suitable for use in a nutrition assignment, personal meal planning project, or AI food-content generation workflow.
