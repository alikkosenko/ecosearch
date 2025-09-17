function showOverlay() {
    document.getElementById("overlay").style.display = "flex";
}

function hideOverlay() {
    document.getElementById("overlay").style.display = "none";
}

// При сабмите формы
document.getElementById("searchForm").addEventListener("submit", function() {
    showOverlay();
});

// Для быстрых кнопок
function quickSearch(text) {
    const input = document.getElementById('searchInput');
    input.value = text;
    //showOverlay();   // ✅ теперь работает
    document.getElementById('searchForm').submit();
}

function copyText(element) {
    const text = element.innerText;
    navigator.clipboard.writeText(text).then(() => {
        element.style.backgroundColor = "#d4edda";
        setTimeout(() => element.style.backgroundColor = "", 500);
    }).catch(err => {
        console.error("Ошибка копирования: ", err);
    });
}
