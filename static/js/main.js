document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const dynamicResults = document.getElementById("dynamicResults");
    let searchTimer;

    if (!searchInput) {
        return;
    }

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.trim();
        searchInput.classList.toggle("is-valid", query.length > 1);

        if (!dynamicResults) {
            return;
        }

        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => {
            fetch(`/search/?q=${encodeURIComponent(query)}`, {
                headers: { "X-Requested-With": "XMLHttpRequest" },
            })
                .then((response) => response.text())
                .then((html) => {
                    dynamicResults.innerHTML = html;
                });
        }, 250);
    });
});
