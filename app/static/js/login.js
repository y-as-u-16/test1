{
  // ユーザー名とパスワードを入れるテキストボックスをおしゃれにするJS
  document.querySelectorAll('input').forEach(input => {
    // フォーカスが当たったとき
    input.addEventListener('focusin', () => {
      input.parentNode.querySelector('label').classList.add('active');
    });
    // フォーカスが外れたとき
    input.addEventListener('focusout', () => {
      if (!input.value) {
        input.parentNode.querySelector('label').classList.remove('active');
      }
    });
  });

  // 新規登録ボタン
  signUpBtn = document.getElementById("signUpBtn");
  // 新規登録ボタンがクリックされたら、新規登録ページにいどうする
  signUpBtn.addEventListener('click', function () {
    window.location.href = '/signup'; // ここに移動したいページのURLを書く
  });
}