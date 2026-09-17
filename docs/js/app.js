const detailTitle = document.getElementById("detail-title");
const detailCategory = document.getElementById("detail-category");
const detailFile = document.getElementById("detail-file");
const codeContent = document.getElementById("code-content");
const loadStatus = document.getElementById("load-status");
const outputContent = document.getElementById("output-content");
const runButton = document.getElementById("run-button");
const fileLinks = document.querySelectorAll(".file-link");

let currentPythonCode = "";
let pyodideReadyPromise;

function getPythonFileUrl(relativePath) {
    if (window.location.hostname.endsWith("github.io")) {
        const repositoryName = window.location.pathname.split("/").filter(Boolean)[0];
        const userName = window.location.hostname.split(".")[0];
        return `https://raw.githubusercontent.com/${userName}/${repositoryName}/main/${relativePath}`;
    }
    return `../${relativePath}`;
}

function appendOutput(text) {
    if (outputContent.textContent === "Programm wird ausgeführt ...") {
        outputContent.textContent = "";
    }
    outputContent.textContent += `${text}\n`;
    outputContent.scrollTop = outputContent.scrollHeight;
}

function updateRunButton() {
    runButton.disabled = currentPythonCode.length === 0;
}

async function initializePython() {
    outputContent.textContent = "Python wird vorbereitet ...";
    runButton.disabled = true;
    try {
        const pyodide = await loadPyodide();
        pyodide.setStdout({ batched: appendOutput });
        pyodide.setStderr({ batched: appendOutput });
        outputContent.textContent = "Python ist bereit.";
        updateRunButton();
        return pyodide;
    } catch (error) {
        outputContent.textContent = `Python konnte nicht gestartet werden.\n\n${error}`;
        throw error;
    }
}

async function runCurrentPythonCode() {
    if (!currentPythonCode) {
        outputContent.textContent = "Es wurde noch keine Python-Datei geladen.";
        return;
    }
    runButton.disabled = true;
    outputContent.textContent = "Programm wird ausgeführt ...";
    try {
        const pyodide = await pyodideReadyPromise;
        await pyodide.runPythonAsync(currentPythonCode);
        if (outputContent.textContent === "Programm wird ausgeführt ...") {
            outputContent.textContent = "Das Programm wurde ohne Ausgabe beendet.";
        }
    } catch (error) {
        outputContent.textContent += `\n\nPython-Fehler:\n${error}`;
    } finally {
        updateRunButton();
    }
}

async function loadPythonFile(button) {
    fileLinks.forEach((link) => link.classList.remove("active"));
    button.classList.add("active");
    detailTitle.textContent = button.dataset.title;
    detailCategory.textContent = button.dataset.category;
    detailFile.textContent = button.dataset.file;
    currentPythonCode = "";
    codeContent.textContent = "Python-Datei wird geladen ...";
    loadStatus.textContent = "Wird geladen ...";
    updateRunButton();
    try {
        const response = await fetch(getPythonFileUrl(button.dataset.path));
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        currentPythonCode = await response.text();
        codeContent.textContent = currentPythonCode;
        loadStatus.textContent = "Datei geladen";
        updateRunButton();
        await pyodideReadyPromise;
        await runCurrentPythonCode();
    } catch (error) {
        codeContent.textContent = `Die Python-Datei konnte nicht geladen werden.\n\nGeprüfter Pfad: ${button.dataset.path}\nFehler: ${error.message}`;
        loadStatus.textContent = "Ladefehler";
        outputContent.textContent = "Die Datei konnte nicht ausgeführt werden.";
        console.error(error);
    }
}

fileLinks.forEach((button) => button.addEventListener("click", () => loadPythonFile(button)));
runButton.addEventListener("click", runCurrentPythonCode);
pyodideReadyPromise = initializePython();

const initiallySelectedFile = document.querySelector(".file-link.active");
if (initiallySelectedFile) loadPythonFile(initiallySelectedFile);

console.log("Python-Lernarchiv gestartet");
