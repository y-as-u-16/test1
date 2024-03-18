{
  document.querySelectorAll('input').forEach(input => {
    input.addEventListener('focusin', () => {
      input.parentNode.querySelector('label').classList.add('active');
    });
  
    input.addEventListener('focusout', () => {
      if (!input.value) {
        input.parentNode.querySelector('label').classList.remove('active');
      }
    });
  });
  
}