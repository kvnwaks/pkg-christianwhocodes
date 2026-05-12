# Lesson 19: Real-World Challenge - Logo Animation

**Section C: Transforms and Scaling** | Lesson 19 of 6

## 🎯 Learning Objectives

By completing this lesson, you will be able to:

- Apply learned concepts to a practical challenge
- Build a real-world component or effect
- Strengthen problem-solving skills with CSS animations

## 📚 Key Concepts

- The `transform` property
- Translation with `translate()`, `translateX()`, `translateY()`
- Scaling with `scale()`, `scaleX()`, `scaleY()`
- Skewing with `skew()`, `skewX()`, `skewY()`

## 📖 Lesson Overview

This practical challenge allows you to demonstrate mastery of the concepts covered. Work through the requirements methodically, building and testing your solution incrementally.

## 💻 Code Examples

### Starting Code

**HTML** (`begin.html`):

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="end.css" />
    <title>Transforms - Real-World Challenge</title>
  </head>
  <body>
    <div class="logo">
      <div class="box box-red"></div>
      <div class="box box-blue"></div>
      <div class="box box-green"></div>
      <div class="box box-orange"></div>
    </div>

    <!-- Transforms Challenge
--------------------

Your task is to create an animation that uses transforms to animate the logo displayed on the page. It should be moved to the middle, stretched on the X axis to elongate the boxes, and *skewed* to make it look like it is tilted ~80 degrees counterclockwise(from the 12 position on a clock). The animation should run once and the logo should retain its styles once the animation is complete. Other than that, expirement with the values! Play around and see what looks best. Good luck! -->
  </body>
</html>
```

**CSS** (`begin.css`):

```css
body {
  margin: 0;
  background: #242423;
}

.box {
  height: 30px;
  width: 30px;
}

.box-red {
  background: #ff4d4d;
  margin: 0;
}

.box-blue {
  background: #738cff;
  margin: 0;
}

.box-green {
  background: #46ff36;
  margin: 0;
}

.box-orange {
  background: #ffaf24;
  margin: 0;
}
```

### Completed Code

**CSS** (`end.css`):

```css
body {
  margin: 0;
  background: #242423;
}

.box {
  height: 30px;
  width: 30px;
  animation: move 2s ease-in-out 1s infinite alternate both;
}

.box-red {
  background: #ff4d4d;
  margin: 0;
}

.box-blue {
  background: #738cff;
  margin: 0;
}

.box-green {
  background: #46ff36;
  margin: 0;
}

.box-orange {
  background: #ffaf24;
  margin: 0;
}

@keyframes move {
  to {
    transform: translate(50vw, 50vh) scaleX(10) skewY(60deg);
  }
}
```

### 🔄 What Changed

**New CSS rules added:**

- `@keyframes move {`
- `to {`

**New properties applied:**

- `animation: move 2s ease-in-out 1s infinite alternate both;`
- `transform: translate(50vw, 50vh) scaleX(10) skewY(60deg);`

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

- [← Previous: Lesson 18](../18-Transform-Challenge/)
- [→ Next Section: Section D: Good to Know](../../D-Good-to-Know/README.md)
- [↑ Section Overview](../README.md)
- [↑ Course Home](../../README.md)
