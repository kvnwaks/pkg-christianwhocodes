# Lesson 6: Real-World Challenge - Menu

**Section A: Transitions** | Lesson 6 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- Using CSS pseudo-classes (`:hover`, `:active`, `:focus`)
- The `transition` property and its syntax
- Timing functions (ease, linear, ease-in, ease-out, ease-in-out)
- Transition shorthand syntax

## 📖 Lesson Overview

This practical challenge allows you to demonstrate mastery of the concepts covered. Work through the requirements methodically, building and testing your solution incrementally.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

```html
<!doctype html>
<html>
  <head>
    <link
      href="https://fonts.googleapis.com/css?family=Roboto&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" type="text/css" href="begin.css" />
    <title>Transitions - Real-World Challenge</title>
  </head>
  <body>
    <div class="title-wrapper">
      <h1 class="title">The Website!</h1>
    </div>
    <div class="menu">
      <div class="menu-item"><a href="#" class="menu-link">Home</a></div>
      <div class="menu-item"><a href="#" class="menu-link">About Us</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Services</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Portfolio</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Contact Us</a></div>
    </div>
    <img
      src="https://wp-assets.futurism.com/2019/10/elon-musk-donates-million-trees-1200x630.jpg"
      class="image"
    />

    <!-- Transitions Challenge
---------------------

The goal of this challenge is to add two transitions to the website; one to the title to change its color to #1f93ff on hover, and another to the menu items to make them grow to 2.5em *and* change color to #1f93ff on hover. Transitions will be added from the ground up, including pseudoselectors and the transitions themselves. All transitions need to have a duration of 1 second and use the ease-out timing function. Good luck! -->
  </body>
</html>
```

**CSS** (`begin.css`):

```css
body {
  margin: 0;
  padding: 0;
}

.menu {
  margin: 0;
  width: 100%;
  padding: 5px;
  background: #bdceff;
  min-height: 10vh;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-content: center;
  border-bottom: 3px solid #005aad;
  flex-wrap: wrap;
}

.menu-link {
  text-decoration: none;
  font-size: 2em;
  text-transform: uppercase;
  font-weight: 800;
  font-family: Roboto, sans-serif;
  color: black;
}

.menu-item {
  height: 3em;
  align-self: center;
  margin: 5px;
}

.title-wrapper {
  margin: 0;
  background: #bdceff;
  border-bottom: 3px solid #005aad;
  padding: 10px;
}

.title {
  margin: 0;
  width: 100%;
  font-weight: 800;
  font-family: Roboto, sans-serif;
  color: black;
  text-transform: uppercase;
  font-size: 4em;
  text-align: center;
}

.image {
  width: 100%;
}
```

### Completed Code

**HTML** (`end.html`):

```html
<!doctype html>
<html>
  <head>
    <link
      href="https://fonts.googleapis.com/css?family=Roboto&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" type="text/css" href="end.css" />
    <title>Transitions - Real-World Challenge</title>
  </head>
  <body>
    <div class="title-wrapper">
      <h1 class="title">The Website!</h1>
    </div>
    <div class="menu">
      <div class="menu-item"><a href="#" class="menu-link">Home</a></div>
      <div class="menu-item"><a href="#" class="menu-link">About Us</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Services</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Portfolio</a></div>
      <div class="menu-item"><a href="#" class="menu-link">Contact Us</a></div>
    </div>
    <img
      src="https://wp-assets.futurism.com/2019/10/elon-musk-donates-million-trees-1200x630.jpg"
      class="image"
    />

    <!-- Transitions Challenge
---------------------

The goal of this challenge is to add two transitions to the website; one to the title to change its color to #1f93ff on hover, and another to the menu items to make them grow to 2.5em *and* change color to #1f93ff on hover. Transitions will be added from the ground up, including pseudoselectors and the transitions themselves. All transitions need to have a duration of 1 second and use the ease-out timing function. Good luck! -->
  </body>
</html>
```

**CSS** (`end.css`):

```css
body {
  margin: 0;
  padding: 0;
}

.menu {
  margin: 0;
  width: 100%;
  padding: 5px;
  background: #bdceff;
  min-height: 10vh;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-content: center;
  border-bottom: 3px solid #005aad;
  flex-wrap: wrap;
}

.menu-link {
  text-decoration: none;
  font-size: 2em;
  text-transform: uppercase;
  font-weight: 800;
  font-family: Roboto, sans-serif;
  color: black;
  /* Add transition */
  transition-property: color, font-size;
  transition-duration: 1s;
  transition-timing-function: ease-in-out;
}

/* Add hover pseudo state */
.menu-link:hover {
  color: #1f93ff;
  font-size: 2.5em;
}

.menu-item {
  height: 3em;
  align-self: center;
  margin: 5px;
}

.title-wrapper {
  margin: 0;
  background: #bdceff;
  border-bottom: 3px solid #005aad;
  padding: 10px;
}

.title {
  margin: 0;
  width: 100%;
  font-weight: 800;
  font-family: Roboto, sans-serif;
  color: black;
  text-transform: uppercase;
  font-size: 4em;
  text-align: center;
  /* Add transition */
  transition: color 1s ease-out;
}

/* Add hover pseudo state */
.title:hover {
  color: #1f93ff;
}

.image {
  width: 100%;
}
```

### 🔄 What Changed

**New CSS rules added:**

- `.menu-link:hover {`
- `.title:hover {`

**New properties applied:**

- `color: #1f93ff;`
- `font-size: 2.5em;`
- `transition-duration: 1s;`
- `transition-timing-function: ease-in-out;`
- `transition: color 1s ease-out;`

**Result:** The element now has enhanced styling and animation behavior.

## 🎯 Challenge

This challenge tests your understanding of the concepts covered. Work through the requirements systematically:

1. Review the starting code
2. Plan your approach
3. Implement the solution incrementally
4. Test frequently in the browser
5. Refine and polish your code
6. Compare with the solution when complete

## ⚡ Practice

1. Open `begin.html` in your browser
2. Open `begin.css` in your code editor
3. Implement the techniques described above
4. Experiment with different values
5. Compare your result with `end.css`

## 🔗 Navigation

- [← Previous: Lesson 5](../05-Transition-Challenge/)
- [→ Next Section: Section B: Animations](../../B-Animations/README.md)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
