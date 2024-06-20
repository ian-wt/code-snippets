// Article:https://ianwaldron.com/article/46/simple-callout-boxes-for-info-tldr-and-so-on/
// Codepen: https://codepen.io/Ian-Waldron/pen/yLWKagW

// add icon and label to parent

const tldrContent = '<i class="fa fa-bolt"></i>tldr:'
const infoContent = '<i class="fa fa-info-circle"></i>info:'

const targets = document.querySelectorAll('.tldr, .info')

targets.forEach(parent => {
  const child = document.createElement('span')
  child.classList.add('icon')
  if (parent.classList.contains('tldr')) {
    child.innerHTML = tldrContent
    parent.prepend(child)
  } else if (parent.classList.contains('info')) {
    child.innerHTML = infoContent
    parent.prepend(child)
  }
})