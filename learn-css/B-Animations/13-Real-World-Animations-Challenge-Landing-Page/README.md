# Lesson 13: Real-World Challenge - Landing Page

**Section B: Animations** | Lesson 13 of 7

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- Core CSS animation concepts

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
      href="https://fonts.googleapis.com/css?family=Sen&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" type="text/css" href="begin.css" />
    <title>Animations - Real-World Challenge</title>
  </head>
  <body>
    <div class="image-wrapper">
      <h1 class="title">Be the best version of you.</h1>
    </div>

    <!-- Animation Challenge
-------------------

Your task is to create two animations that will first cause the background to fade in and expand in width from left to right, then fade in the text in the center. The first animation should take 1.5 seconds, followed by a 0.5 second delay, and finally, 1 second for the text fade-in. Both animations should have an ease-out timing function and run once. All styles should be retained once the animation ends. Good luck! -->
  </body>
</html>
```

**CSS** (`begin.css`):

```css
body {
  margin: 0;
}

.image-wrapper {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: url("main.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.title {
  font-size: 4em;
  text-transform: uppercase;
  margin: 0;
  font-family: Sen;
  text-align: center;
}
```

### Completed Code

**HTML** (`end.html`):

```html
<!doctype html>
<html>
  <head>
    <link
      href="https://fonts.googleapis.com/css?family=Sen&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" type="text/css" href="end.css" />
    <title>Animations - Real-World Challenge</title>
  </head>
  <body>
    <div class="image-wrapper">
      <h1 class="title">Be the best version of you.</h1>
    </div>

    <!-- Animation Challenge
-------------------

Your task is to create two animations that will first cause the background to fade in and expand in width from left to right, then fade in the text in the center. The first animation should take 1.5 seconds, followed by a 0.5 second delay, and finally, 1 second for the text fade-in. Both animations should have an ease-out timing function and run once. All styles should be retained once the animation ends. Good luck! -->
  </body>
</html>
```

**CSS** (`end.css`):

```css
body {
  margin: 0;
}

.image-wrapper {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: url("main.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  animation-name: expand-fade-in;
  animation-duration: 1.5s;
  animation-timing-function: ease-out;
  animation-fill-mode: both;
}

.title {
  font-size: 4em;
  text-transform: uppercase;
  margin: 0;
  font-family: Sen;
  text-transform: uppercase;
  text-align: center;
  animation-name: fade-in;
  animation-duration: 1s;
  animation-timing-function: ease-out;
  animation-fill-mode: both;
  animation-delay: 2s; /* Delay caters for the animation-duration of image-wrapper */
}

@keyframes expand-fade-in {
  from {
    opacity: 0%;
    width: 0%;
  }
  to {
    opacity: 100%;
    width: 100%;
  }
}

@keyframes fade-in {
  from {
    opacity: 0%;
  }
  to {
    opacity: 100%;
  }
}
```

### 🔄 What Changed

**New CSS rules added:**

- `@keyframes expand-fade-in {`
- `@keyframes fade-in {`
- `from {`
- `to {`

**New properties applied:**

- `animation-duration: 1.5s;`
- `animation-duration: 1s;`
- `opacity: 100%;`
- `width: 0%;`
- `width: 100%;`

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

- [← Previous: Lesson 12](../12-Animation-Challenge/)
- [→ Next Section: Section C: Transforms and Scaling](../../C-Transforms-and-Scaling/README.md)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
