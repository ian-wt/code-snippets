const rows = document.querySelectorAll('.journal-entry tr:not(:first-child)')

document.addEventListener('DOMContentLoaded', () => {
  rows.forEach(row => {
    const [first, second, third] = row.querySelectorAll('td')
    if ([first, second, third].every(Boolean)) {
      // make sure the elements we need exist
      first.textContent = first.textContent.trim();
      if (third.textContent.trim() !== '' && second.textContent.trim() === '') {
        // indent credits by set amount
        // first.style = 'padding-left: 2rem;'
        // do it dynamically instead
        const leftPadding = parseFloat(getComputedStyle(first).paddingLeft);
        // indent left the greater of atleast 3x existing padding or 25px
        first.style.paddingLeft = Math.max((leftPadding * 3), 25) + 'px'
      }
    }
  })
})
