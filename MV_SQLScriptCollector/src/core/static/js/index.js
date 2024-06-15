document.addEventListener('DOMContentLoaded', (event) => {
    const scriptLinks = document.querySelectorAll('.script-link');
    const searchInput = document.getElementById('searchInput');

    scriptLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const scriptName = e.target.getAttribute('data-script-name');
            const scriptText = e.target.getAttribute('data-script-text');
            const scriptAuthor = e.target.getAttribute('data-script-author');
            const scriptCreated = e.target.getAttribute('data-script-created');
            const scriptModified = e.target.getAttribute('data-script-modified');
            const scriptDescription = e.target.getAttribute('data-script-description');

            document.querySelector('.script-name').textContent = scriptName;
            document.querySelector('.script-text').textContent = scriptText;
            document.querySelector('#author-info').textContent = "Автор: " + scriptAuthor;
            document.querySelector('#created-info').textContent = "Дата создания: " + scriptCreated;
            document.querySelector('#modified-info').textContent = "Дата последнего изменения: " + scriptModified;
            document.querySelector('#name-info').textContent = "Название: " + scriptName;
            document.querySelector('#description-info').textContent = "Описание: " + scriptDescription;
        });
    });

    searchInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && searchInput.value.trim().toLowerCase() !== '') {
            collapseAll();
            performSearch();
        } else {
            collapseAll();
        }
    });

    function collapseAll() {
        const collapseItems = document.querySelectorAll('.collapse');
        collapseItems.forEach(item => {
            if (item.classList.contains('show')) {
                const button = item.previousElementSibling;
                button.click();
            }
        });
    }

function performSearch() {
    const searchText = searchInput.value.trim().toLowerCase();

    const parentButtons = document.querySelectorAll('.btn-toggle');
    const collapseItems = document.querySelectorAll('.collapse');

    parentButtons.forEach(button => {
        button.setAttribute('aria-expanded', 'false');
        button.classList.add('collapsed'); // Шаг 2
    });

    collapseItems.forEach(item => {
        item.classList.remove('show'); // Шаг 2
    });

    parentButtons.forEach(button => {
        let hasMatchingScript = false;
        const childScripts = button.nextElementSibling.querySelectorAll('.script-link');

        childScripts.forEach(link => {
            const scriptName = link.getAttribute('data-script-name').toLowerCase();
            if (scriptName.includes(searchText)) {
                hasMatchingScript = true;
            }
        });

        if (hasMatchingScript) {
            button.setAttribute('aria-expanded', 'true');
            button.classList.remove('collapsed'); // Шаг 3
            button.nextElementSibling.classList.add('show'); // Шаг 3
        }
    });

    scriptLinks.forEach(link => {
        const scriptName = link.getAttribute('data-script-name').toLowerCase();
        const spanElement = link.closest('.script-name');

        if (scriptName.includes(searchText)) {
            spanElement.style.display = ''; // Показываем элемент, если он подходит под поиск (Шаг 4)
        } else {
            spanElement.style.display = 'none'; // Скрываем элемент, если он не подходит под поиск (Шаг 4)
        }
    });
}



});

document.addEventListener('DOMContentLoaded', function() {
    const copyButton = document.getElementById('copy-button');
    const scriptText = document.querySelector('.script-text');

    copyButton.addEventListener('click', function() {
        const text = scriptText.innerText;
        navigator.clipboard.writeText(text).then(function() {
            console.log('Text copied to clipboard');
        }).catch(function(err) {
            console.error('Could not copy text: ', err);
        });
    });
});

