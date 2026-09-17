const detailTitle = document.getElementById("detail-title");
const detailCategory = document.getElementById("detail-category");
const detailFile = document.getElementById("detail-file");
const codeContent = document.getElementById("code-content");
const loadStatus = document.getElementById("load-status");
const fileLinks = document.querySelectorAll(".file-link");

function getPythonFileUrl(relativePath) {
    const isGitHubPages = window.location.hostname.endsWith("github.io");

    if (isGitHubPages) {
        const repositoryName = window.location.pathname.split("/").filter(Boolean)[0];
        const userName = window.location.hostname.split(".")[0];

        return `https://raw.githubusercontent.com/${userName}/${repositoryName}/main/${relativePath}`;
    }

    return `../${relativePath}`;
}

async function loadPythonFile(button) {
    fileLinks.forEach((link) => link.classList.remove("active"));
    button.classList.add("active");

    detailTitle.textContent = button.dataset.title;
    detailCategory.textContent = button.dataset.category;
    detailFile.textContent = button.dataset.file;

    codeContent.textContent = "Python-Datei wird geladen ...";
    loadStatus.textContent = "Wird geladen ...";

    try {
        const fileUrl = getPythonFileUrl(button.dataset.path);
        const response = await fetch(fileUrl);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        codeContent.textContent = await response.text();
        loadStatus.textContent = "Datei geladen";
    } catch (error) {
        codeContent.textContent = `Die Python-Datei konnte nicht geladen werden.\n\nGeprüfter Pfad: ${button.dataset.path}\nFehler: ${error.message}`;
        loadStatus.textContent = "Ladefehler";
        console.error("Python-Datei konnte nicht geladen werden:", error);
    }
}

fileLinks.forEach((button) => {
    button.addEventListener("click", () => loadPythonFile(button));
});

const initiallySelectedFile = document.querySelector(".file-link.active");

if (initiallySelectedFile) {
    loadPythonFile(initiallySelectedFile);
}

console.log("Python-Lernarchiv gestartet");
