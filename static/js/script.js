function quickSearch(text) {
        // Подставляем текст в поле поиска
        document.getElementById('searchInput').value = text;
        // Отправляем форму
        document.getElementById('searchForm').submit();
}

function copyText(element) {
    const text = element.innerText;  // Берём текст из <td>
    navigator.clipboard.writeText(text).then(() => {
        // Можно добавить подсветку или уведомление
        element.style.backgroundColor = "#d4edda";
        setTimeout(() => element.style.backgroundColor = "", 500);
    }).catch(err => {
        console.error("Ошибка копирования: ", err);
    });
}
