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

function editReserve(cell, row) {
    let currentValue = cell.innerText.trim();
    let newValue = prompt("Введите новое значение резерва:", currentValue);

    if (newValue !== null) {
        // 1. Меняем сразу на странице
        cell.innerText = newValue;

        // 2. Отправляем на сервер
        fetch("/update_reserve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                row: row,       // строка из item
                value: newValue // новое значение
            })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                alert("Ошибка при сохранении: " + data.error);
            }
        })
        .catch(err => {
            console.error("Ошибка запроса:", err);
            alert("Не удалось обновить резерв.");
        });
    }
}

