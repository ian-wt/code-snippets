// Article: https://ianwaldron.com/article/50/add-form-to-django-formset-dynamically-with-javascript/
// Codepen: https://codepen.io/Ian-Waldron/pen/bGPNpBB


// clone form

class FormNotFoundError extends Error {
  constructor(message) {
    super(message)
    this.name = 'FormNotFoundError'
  }
}

class TooManyFormsError extends Error {
  constructor(message) {
    super(message)
    this.name = 'TooManyFormsError'
  }
}

function cloneForm(selector, prefix, remove_checked = true, additionalFn) {
  // grab the last item using pop() so we can append after/bottom
  // 'pop' method isn't avaialble to nodelist so we need to convert to array
  const ancestor = [...document.querySelectorAll(selector)].pop()
  // or convert nodelist to array this way
  // const ancestor = Array.from(document.querySelectorAll(selector)).pop()
  if (ancestor) {
    // at least one element matching the selector exists
    const maxForms = document.querySelector('input[name$="-MAX_NUM_FORMS"]')
    const totalElement = document.querySelector('input[name$="-TOTAL_FORMS"]')
    if (maxForms.value === totalElement.value) {
      // we're already at the limit
      throw new TooManyFormsError('Unable to add additional form. ' +
                                  'Max Forms threshold has been met')
    } else {

      const newForm = ancestor.cloneNode(true)
      // use regex so me don't need to match ancestor num for replace to work
      const regex = RegExp(`${ prefix }-(\\d+)-`)
      let total = totalElement.value

      // grab all commonly encountered input types
      // exludes the less common types like 'progress,' etc.
      newForm.querySelectorAll('input, select, textarea').forEach((input) => {
        const name = input.getAttribute('name').replace(regex, `${ prefix }-${ total}-`)
        const id = `id_${ name }`
        input.setAttribute('name', name)
        input.setAttribute('id', id)
        // clear any values already entered in ancestor
        input.value = ''
        // otherwise, closed form will inherit checked state of ancestor
        if (remove_checked) {
          input.removeAttribute('checked')
        }
      })

      // update references for label
      newForm.querySelectorAll('label').forEach((label) => {
        const newFor = label.getAttribute('for').replace(regex, `${ prefix }-${ total}-`)
        label.setAttribute('for', newFor)
      })

      total++;
      totalElement.value = total;

      // additional functionality
      if (additionalFn) {
        // allow the exception if not a function
        additionalFn({
          'newForm': newForm,
          'ancestor': ancestor,
          'total': total
        })
      }
      ancestor.after(newForm)
    }
  } else {
    // couldn't find an element to clone
    throw new FormNotFoundError('Unable to retrive existing form to clone. ' +
                                'Check your selector is correc and at least one form exists.')
  }
}